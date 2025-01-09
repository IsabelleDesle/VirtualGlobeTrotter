import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import subprocess
import time
from typing import Optional, List, Dict, Any

class VGT:
    def __init__(self, elasticsearch_url: str = "http://localhost:9200/"):
        self.elasticsearch_url = elasticsearch_url
        self.client = None
        self.default_index = "images"
        
    def start_docker_services(self) -> None:
        """Start Docker services using docker-compose."""
        command = ["docker", "compose", "up", "--build", "-d"]
        try:
            subprocess.run(command, check=True)
            print("Docker Compose up --build executed successfully! Waiting for services to start...")
            time.sleep(40)  # Wait for services to initialize
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to start Docker services: {e}")

    def connect_to_elasticsearch(self) -> None:
        """Establish connection to Elasticsearch."""
        self.client = Elasticsearch(self.elasticsearch_url)
        if not self.client.ping():
            raise ConnectionError("Failed to connect to Elasticsearch")
        print("Connected to Elasticsearch!")

    def load_data_from_csv(self, csv_file: str, delimiter: str = ";") -> List[Dict[str, Any]]:
        """
        Load and process data from CSV file.
        Returns: List[Dict]: List of records from CSV
        """
        try:
            df = pd.read_csv(csv_file, delimiter=delimiter)
            return df.to_dict(orient="records")
        except Exception as e:
            raise ValueError(f"Failed to load CSV file: {e}")

    def upload_to_elasticsearch(self, records: List[Dict], index_name: Optional[str] = None) -> None:
        """
        Upload data to Elasticsearch index.
        Args:
            records (List[Dict]): Data to upload
            index_name (str, optional): Name of the index
        """
        if not self.client:
            raise RuntimeError("Elasticsearch client not initialized. Call connect_to_elasticsearch() first.")
            
        index_name = index_name or self.default_index
        
        actions = [
            {
                "_index": index_name,
                "_source": record
            }
            for record in records
        ]

        try:
            if not self.client.indices.exists(index=index_name):
                self.client.indices.create(index=index_name)

            bulk(self.client, actions)
            print(f"Data uploaded successfully to index '{index_name}'!")
        except Exception as e:
            raise RuntimeError(f"Failed to upload data to Elasticsearch: {e}")

    def read_search_terms(self, filename: str) -> str:
        """
        Read and process search terms from JSON file.
        Returns: str: Processed search terms
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return " ".join([entry["text"] for entry in data])
        except FileNotFoundError:
            print(f"Warning: File {filename} not found. Using default search term.")
            return "Disney"
        except Exception as e:
            raise ValueError(f"Failed to read search terms: {e}")

    def search_images(self, search_terms: str, output_file: str, index: Optional[str] = None) -> None:
        # Search images in Elasticsearch and save results.
        # Args:
        #     search_terms (str): Terms to search for
        #     output_file (str): Path to output JSON file
        #     index (str, optional): Index to search in
        if not self.client:
            raise RuntimeError("Elasticsearch client not initialized. Call connect_to_elasticsearch() first.")
            
        index = index or self.default_index
        
        try:
        # search in title, content and tags fields.
        # take the result with the highest relevance score
            query = {
                "query": {
                    "multi_match": {
                        "query": search_terms,
                        "fields": ["title", "content", "tags"]
                    }
                },
                "size": 1,
                "sort": [{"_score": {"order": "desc"}}]
            }

            response = self.client.search(index=index, body=query)
            
            if response["hits"]["hits"]:
                self._process_and_save_results(response["hits"]["hits"], output_file)
            else:
                print("No results found.")
        except Exception as e:
            raise RuntimeError(f"Search failed: {e}")

    def _process_and_save_results(self, results: List[Dict], output_file: str) -> None:
        """
        Process search results and save to file.
        
        Args:
            results (List[Dict]): Search results
            output_file (str): Path to output file
        """
        for result in results:
            print(f"ID: {result['_id']}")
            print(f"Title: {result['_source']['title']}")
            print(f"Tags: {result['_source']['tags']}")
            print(f"Content: {result['_source']['content']}")
            print(f"Relevance Score: {result['_score']}")
            print(f"Image Path: {result['_source']['image_path']}\n")

            try:
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
            except Exception as e:
                raise IOError(f"Failed to process or save results: {e}")

    def run_interactive_search(self, initial_input_file: str, output_file: str) -> None:
        """
        Run interactive search session.
        
        Args:
            initial_input_file (str): Path to initial search terms file
            output_file (str): Path to output file
        """
        try:
            search_terms = self.read_search_terms(initial_input_file)
            self.search_images(search_terms, output_file)

            while True:
                user_input = input("Another search? Press Enter to continue or type 'No' to stop: ")
                if user_input.lower() == "no":
                    break
                if user_input:
                    self.search_images(user_input, output_file)
        except KeyboardInterrupt:
            print("\nSearch session terminated by user.")