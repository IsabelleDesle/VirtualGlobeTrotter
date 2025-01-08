from huggingface_hub import InferenceClient
from PIL import Image
import time
import io
import time
import Constants
#
#  Model too busy to make inference
#

start = time.time()

client = InferenceClient(model="strangerzonehf/Flux-Midjourney-Mix2-LoRA",
                         token=Constants.HUGGINGFACE_API_KEY)

print(f"Client created in {time.time()- start} seconds")

response = client.text_to_image(
    prompt="MJ v6, beautiful Canada forest landscape in the style of nature photography, scenic view, 8k --ar 16:9",
    # height=576,
    # width=1024,
    # num_inference_steps=28,
    # model="jbilcke-hf/flux-dev-panorama-lora-2",
    # guidance_scale=7.5,
    # target_size=(1024, 768),
    # seed=42
)

print(f"Response received in {time.time()- start} seconds")

print(response)

# image = Image.open(io.BytesIO(response))

response.save(r".images/flux-midjourney/canada_forest.jpg")

