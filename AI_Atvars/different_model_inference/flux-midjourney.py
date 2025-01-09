from huggingface_hub import InferenceClient
from PIL import Image
import time
import io
import time
import sys
import os
sys.path.insert(0, os.path.abspath('./AI_Atvars/'))
import Constants
import datetime
#
#  Model too busy to make inference
#

start = time.time()

client = InferenceClient(model="strangerzonehf/Flux-Midjourney-Mix2-LoRA",
                         token=Constants.HUGGINGFACE_API_KEY)

print(f"Client created in {time.time()- start} seconds")

response = client.text_to_image(
    prompt="MJ v6, beautiful and serene winter Canada forest landscape in the style of nature photography, scenic view, 8k --ar 2:1",
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

save_path = os.path.abspath('./AI_Atvars/images/flux-midjourney/{0}.jpg'.format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))
response.save(save_path)

