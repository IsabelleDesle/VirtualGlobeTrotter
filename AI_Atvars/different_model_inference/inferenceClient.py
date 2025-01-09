from huggingface_hub import InferenceClient
from PIL import Image
import time
import io
import time

# To import the Constants file, I had to add the path to the sys.path, so that it could find the file
import sys
import os
sys.path.insert(0, os.path.abspath('./AI_Atvars/'))
import Constants
#
#   General inference client, the first model I tried, which was the one that had the eerie pictures of the forest
#

start = time.time()

client = InferenceClient(model="jbilcke-hf/flux-dev-panorama-lora-2",
                         token=Constants.HUGGINGFACE_API_KEY)

print(f"Client created in {time.time()- start} seconds")

response = client.text_to_image(
    #       The HDRI panoramic ... is needed to make the model generate the correct perspective
    prompt="HDRI panoramic view of TOK, tranquil lake in a snowy pine forest in Japan, the water is clear, in the center of the pond is a small island with a cherry blossom tree, photography style, 4k, realistic.",
    height=1024,
    width=2048,
    num_inference_steps=28,
    # model="jbilcke-hf/flux-dev-panorama-lora-2",
    # guidance_scale=7.5,
    # target_size=(1024, 768),
    # seed=42
)

print(f"Response received in {time.time()- start} seconds")

print(response)

# image = Image.open(io.BytesIO(response))

response.save(r"C:\Users\Atvar\Desktop\year2\VirtualGlobeTrotter\AI_Atvars\images\flux-dev\japan_forest.jpg")