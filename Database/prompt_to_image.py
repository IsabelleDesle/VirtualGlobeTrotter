import json
import mysql.connector
import speech_recognition as sr
import time as t

def transcribe_voice_input(output_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use microphone as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)

        start_time = t.time()
        transcriptions = []  # Store transcriptions in a list

        try:
            while True:
                elapsed_time = t.time() - start_time

                print("Listening...")
                print(f"Time elapsed: {elapsed_time:.2f} seconds")

                # Break the loop after 10 seconds
                if elapsed_time > 10:
                    # print("Time limit reached. Stopping transcription.")
                    print("")
                    break

                # Listen to the audio
                audio = recognizer.listen(source)

                try:
                    # Recognize speech using Google Web Speech API
                    text = recognizer.recognize_google(audio, language="en-US")
                    print("You said: " + text)

                    # Append the recognized text to the list
                    transcriptions.append({"timestamp": elapsed_time, "text": text})

                except sr.UnknownValueError:
                    #print("Google Web Speech could not understand audio")
                    print("")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Web Speech service; {e}")

        except KeyboardInterrupt:
            print("Transcription stopped.")

        # Save transcriptions to the output JSON file
        with open(output_file, "w") as f:
            json.dump(transcriptions, f, indent=4)

# Function to read the search terms from a JSON file
def read_search_terms_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            search_terms = " ".join([entry["text"] for entry in data])
        return search_terms
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None

# Function to connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',        # Your MySQL host (e.g., localhost or IP address)
            port="3306",             # Port number (default is 3306)
            user='root',             # Your MySQL username
            password='root',         # Your MySQL password
            database='vgt'          # The database you want to use
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to search for images based on the search terms
def search_images(conn, search_terms, output_file):
    try:
        cursor = conn.cursor(dictionary=True)

        # query = """
        # SELECT id, title, content, tags, continent, image_path, MATCH(title, content, tags) AGAINST(%s) AS relevance
        # FROM images
        # ORDER BY relevance DESC
        # LIMIT 1
        # """


        #Avoid Excessive LIKE Queries: Use them only as a fallback for substring matches.

        query = """
        SELECT id, title, content, tags, continent, image_path, MATCH(title, content, tags) AGAINST(%s) AS relevance
        FROM images 
        WHERE MATCH(title, content, tags) AGAINST(%s)

        UNION ALL
        
        SELECT id, title, tags, content, 0.5 AS relevance
        FROM images 
        WHERE 
        (title LIKE CONCAT('%', %s, '%') 
        OR content LIKE CONCAT('%', %s, '%') 
        OR tags LIKE CONCAT('%', %s, '%'))
        
        AND id NOT IN (
            SELECT id 
            FROM images 
            WHERE MATCH(title, content, tags) AGAINST(%s)
        )
        ORDER BY relevance DESC
        LIMIT 1 
        """

        # Execute the query with the search terms
        cursor.execute(query, (search_terms,))
        results = cursor.fetchall()

        if results:
            print(f"Found {len(results)} result(s):")
            for result in results:
                print(f"ID: {result['id']}")
                print(f"Title: {result['title']}")
                print(f"Relevance: {result['relevance']}")
                print(f"Image Path: {result['image_path']}\n")

                # Append result details to the JSON file
                with open(output_file, "r") as f:
                    transcriptions = json.load(f)

                # Ensure each transcription entry is enriched with the result details
                for transcription in transcriptions:
                    transcription.update({
                        "ID": result['id'],
                        "Title": result['title'],
                        "Relevance": result['relevance'],
                        "Image Path": result['image_path']
                    })

                with open(output_file, "w") as f:
                    json.dump(transcriptions, f, indent=4)

        else:
            print("No results found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Main function to execute the entire process
def main():

    output_file = r"C:\\Users\\desle\\LOCAL_STUFF\\LOC_2S1_005_TEAM_PROJECT\\VirtualGlobeTrotter\\Database\\prompt.json"
   

    transcribe_voice_input(output_file)
    print(f"Transcript saved to {output_file}")
    print("")

    # Read the search terms from the JSON file
    search_terms = read_search_terms_from_file(output_file)
    if not search_terms:
        return

    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Perform the image search
    search_images(conn, search_terms, output_file)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
