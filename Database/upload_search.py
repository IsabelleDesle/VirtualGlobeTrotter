import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import speech_recognition as sr
import time as t

#run compose.yaml first! 
import subprocess

# Define the command
command = ["docker", "compose", "up", "--build", "-d"]

# Execute the command
try:
    subprocess.run(command, check=True)
    print("Docker Compose up --build executed successfully! Wait ... ")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")

t.sleep(40)



# Connect to Elasticsearch
def connect_to_elasticSearch(): 
    client = Elasticsearch("http://localhost:9200/")

    if not client.ping():
        print("Elasticsearch connection failed.")
        exit()

    print("Connected to Elasticsearch!")

    # Load the CSV file into a pandas DataFrame
    csv_file =   "./images_path.csv"
    df = pd.read_csv(csv_file, delimiter=";")

    # Define the index name
    index_name = "images"  # Replace with your desired index name

    # Convert DataFrame to a list of dictionaries
    records = df.to_dict(orient="records")

    # Prepare the data for bulk upload
    actions = [
        {
            "_index": index_name,
            "_source": record
        }
        for record in records
    ]

    # Create the index and upload data
    try:
        # Create index if it doesn't exist
        if not client.indices.exists(index=index_name):
            client.indices.create(index=index_name)

        # Bulk upload
        bulk(client, actions)
        print(f"Data from {csv_file} uploaded successfully to index '{index_name}'!")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return client

def read_search_terms_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            search_terms = " ".join([entry["text"] for entry in data])
            
        return search_terms
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None


def search_images(es, index, search_terms, output_file):
    try:
        query = {
            "query": {
                "multi_match": {
                    "query": search_terms,
                    "fields": ["title", "content", "tags"]
                }
            },
            "size": 1,
            "sort": [
                {"_score": {"order": "desc"}}
            ]
        }

        response = es.search(index=index, body=query)

        if response["hits"]["hits"]:
            print(f"Found {len(response['hits']['hits'])} result(s):")
            results = response["hits"]["hits"]
            for result in results:
                print(f"ID: {result['_id']}")
                print(f"Title: {result['_source']['title']}")
                print(f"Tags: {result['_source']['tags']}")
                print(f"Content: {result['_source']['content']}")
                print(f"Relevance Score: {result['_score']}")
                print(f"Image Path: {result['_source']['image_path']}\n")

                with open(output_file, "r") as f:
                    transcriptions = json.load(f)

                for transcription in transcriptions:
                    transcription.update({
                        "ID": result["_id"],
                        "Title": result["_source"]["title"],
                        "Relevance": result["_score"],
                        "Image Path": result["_source"]["image_path"]
                    })

                with open(output_file, "w") as f:
                    json.dump(transcriptions, f, indent=4)
        else:
            print("No results found.")




    except Exception as e:
        print(f"Error during Elasticsearch search: {e}")


try: 
    input_file = r"./voice_input.json"
    output_file = r"./output.json"
    search_terms = read_search_terms_from_file(input_file)

    if not search_terms:
        search_terms = "Disney"
        
    es = connect_to_elasticSearch()
    search_images(es, index="images", search_terms=search_terms, output_file=output_file)

    while True:
        a = input("another search? Please enter or type No to stop  ")
        if a == "no" or a == "No": 
            break
        else: 
            search_images(es, index="images", search_terms=a, output_file=output_file)
except KeyboardInterrupt:
    print("exit")
             
        



