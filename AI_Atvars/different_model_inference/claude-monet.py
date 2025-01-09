
from huggingface_hub import InferenceClient
from PIL import Image
import time
import io
import time
import sys
import os
sys.path.insert(0, os.path.abspath('./AI_Atvars/'))
import Constants
import datetime # For naming the image
#
#   General inference client, the first model I tried, which was 
#

start = time.time()

client = InferenceClient(model="openfree/claude-monet",
                         token=Constants.HUGGINGFACE_API_KEY)

print(f"Client created in {time.time()- start} seconds")

response = client.text_to_image(
    prompt="A painting of a forest in Canada, in the style of Claude Monet. Large trees fill the landscape, and the ground is covered by moss, ferns, and other plants.",
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


save_path = os.path.abspath('./AI_Atvars/images/claude-monet/{0}.jpg'.format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")))

response.save(save_path)

