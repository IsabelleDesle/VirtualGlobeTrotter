# Python Script (image_sender.py)
import socket
import os
import PIL
from PIL import Image
import io

# PIL.Image.MAX_IMAGE_PIXELS = 933120000 needs to be set
import PIL.Image

def send_image(image_path, host='localhost'
, port=12345):
    # Open and convert image to bytes
    with Image.open(image_path) as img:
        # Convert image to RGB if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

    # Get file name from path
    file_name = os.path.basename(image_path)
    
    try:
        # Create socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            
            # Send filename length and filename
            name_bytes = file_name.encode('utf-8')
            s.send(len(name_bytes).to_bytes(4, 'big'))
            s.send(name_bytes)
            
            # Send image size and image data
            s.send(len(img_byte_arr).to_bytes(4, 'big'))
            s.send(img_byte_arr)
            
            print(f"Image {file_name} sent successfully")
            
    except Exception as e:
        print(f"Error sending image: {e}")

# Example usage
if __name__ == "__main__":
    PIL.Image.MAX_IMAGE_PIXELS = 933120000
    send_image(r"C:\Users\Atvar\Downloads/upscaled_swapped_camels in the desert.jpg")
    # print(PIL.__file__)  # prints, e. g., /usr/lib/python3/dist-packages/PIL/__init__.py
