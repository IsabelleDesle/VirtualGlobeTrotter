import mysql.connector
import speech_recognition as sr
import time as t
#from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def transcribe_voice_input(output_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use microphone as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        

        start_time = t.time()
     
        # Open the output file in append mode
        with open(output_file, "a") as f:
            try:
                while True :
                    elapsed_time = t.time() - start_time
                    
                    


                    print("Listening...") 
                    print(f"Time elapsed: {elapsed_time:.2f} seconds")
                 
                       

                    # Listen to the audio
                    audio = recognizer.listen(source)

                    try:
                        # Recognize speech using Google Web Speech API
                        text = recognizer.recognize_google(audio, language="en-US")
                        print("You said: " + text)
                                            # Break the loop after 10 seconds
                        if elapsed_time > 10:
                            print("Time limit reached. Stopping transcription.")
                            break


                        # Overwrite the recognized text to the output file
                        with open(output_file, "w") as f:
                            f.write(text + "\n")

                    except sr.UnknownValueError:
                        #print("Google Web Speech could not understand audio")
                        if elapsed_time > 5:
                            print("Time limit reached. Stopping transcription.")
                            break

                        break
                    except sr.RequestError as e:
                        print(f"Could not request results from Google Web Speech service; {e}")
                        break

            except KeyboardInterrupt:
                print("Transcription stopped.")
                with open(output_file, "w") as f:
                    f.write("\n[Transcription Ended]\n")

# Function to read the search terms from a text file
def read_search_terms_from_file(filename):
    try:
        with open(filename, 'r') as file:
            search_terms = file.read().strip()
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
            user='root',    # Your MySQL username
            password='root',  # Your MySQL password
            database='vgt2'   # The database you want to use
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to search for images based on the search terms
def search_images(conn, search_terms):
    try:
        cursor = conn.cursor(dictionary=True)
        
        # Perform the full-text search using MATCH ... AGAINST
        # query = """
        # SELECT id, title, content, image_path
        # FROM images
        # WHERE MATCH(title, content, tags) 
        # AGAINST(%s IN NATURAL LANGUAGE MODE)
        # """

        # # # Use MySQL's relevance:
        query = """
        SELECT id, title, content, image_path, MATCH(title, content, tags) AGAINST(%s) AS relevance
        FROM images

        ORDER BY relevance DESC
        LIMIT 1
        
        """
        
        # Execute the query with the search terms
        cursor.execute(query, (search_terms,))
        results = cursor.fetchall()

        # Check if we found any results
        if results:
            print(f"Found {len(results)} result(s):")
            
            for result in results:
                
                print(f"ID: {result['id']}")
                print(f"Title: {result['title']}")
                print(f"Relevance: {result['relevance']}")
                print(f"Image Path: {result['image_path']}\n")

                
        else:
            print("No results found.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        


# Main function to execute the entire process
def main():
    output_file = r"C:\Users\desle\LOCAL_STUFF\LOC_2S1_005_TEAM_PROJECT\prompt.txt"

    transcribe_voice_input(output_file)
    print(f"Transcript saved to {output_file}")
    print("")

    # Read the search terms from the text file
    search_terms = read_search_terms_from_file(output_file)
    if not search_terms:
        return
    
    # Connect to the MySQL database
    conn = connect_to_database()
    if conn is None:
        return
    
    # Perform the image search
    search_images(conn, search_terms)
    
    # Close the connection
    conn.close() 

if __name__ == "__main__":
    main()
    
