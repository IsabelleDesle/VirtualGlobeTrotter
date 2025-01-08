from huggingface_hub import InferenceClient
from PIL import Image
import time
import io
import time
import Constants
#
#   General inference client, the first model I tried, which was the one that had the eerie pictures of the forest
#

start = time.time()

client = InferenceClient(model="jbilcke-hf/flux-dev-panorama-lora-2",
                         token=Constants.HUGGINGFACE_API_KEY)

print(f"Client created in {time.time()- start} seconds")

response = client.text_to_image(
    prompt="HDRI panoramic view of TOK, a small wooden hut with a red roof in the center of the image, two large windows on the front side of the hut, lush green jungle foliage surrounding the hut and the ground, tall trees with thick trunks and sparse leaves in the background, sunlight filtering through the canopy creating patches of light and shadow on the ground, some fallen leaves scattered on the ground, an overall rustic and natural setting, likely a secluded or abandoned dwelling, no visible humans or animals.",
    height=640,
    width=1536,
    num_inference_steps=50,
    # model="jbilcke-hf/flux-dev-panorama-lora-2",
    guidance_scale=7.5,
    # target_size=(1024, 768),
    seed=42
)

print(f"Response received in {time.time()- start} seconds")

print(response)

# image = Image.open(io.BytesIO(response))

response.save(r"./with-vs-without-pe/with-pe.jpg")