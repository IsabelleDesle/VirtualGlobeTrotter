import json
import speech_recognition as sr
import time as t
from elasticsearch import Elasticsearch

def transcribe_voice_input(output_file):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)

        start_time = t.time()
        transcriptions = []

        try:
            while True:
                elapsed_time = t.time() - start_time

                print("Listening...")
                print(f"Time elapsed: {elapsed_time:.2f} seconds")

                if elapsed_time > 10:
                    print("")
                    break

                audio = recognizer.listen(source)

                try:
                    text = recognizer.recognize_google(audio, language="en-US")
                    print("You said: " + text)
                    transcriptions.append({"timestamp": elapsed_time, "text": text})
                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Web Speech service; {e}")

        except KeyboardInterrupt:
            print("Transcription stopped.")

        with open(output_file, "w") as f:
            json.dump(transcriptions, f, indent=4)

def read_search_terms_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            search_terms = " ".join([entry["text"] for entry in data])
            print(f"Search terms: {type(search_terms)}")
        return search_terms
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None

def connect_to_elasticsearch():
    try:
        es = Elasticsearch([{"host": "localhost", "port": 5601}])
        if es.ping():
            print("Connected to Elasticsearch!")
        else:
            print("Failed to connect to Elasticsearch.")
            return None
        return es
    except Exception as e:
        print(f"Error connecting to Elasticsearch: {e}")
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

def main():
    output_file = r"C:\\Users\\desle\\LOCAL_STUFF\\LOC_2S1_005_TEAM_PROJECT\\VirtualGlobeTrotter\\Database\\prompt.json"

    transcribe_voice_input(output_file)
    print(f"Transcript saved to {output_file}")
    print("")

    search_terms = read_search_terms_from_file(output_file)
    if not search_terms:
        return

    es = connect_to_elasticsearch()
    if es is None:
        return

    search_images(es, index="images", search_terms=search_terms, output_file=output_file)

if __name__ == "__main__":
    main()
