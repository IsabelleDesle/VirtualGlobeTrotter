from huggingface_hub import InferenceClient
from PIL import Image
import time
import io
import time
import Constants
#
#   Ghibksy model
# Very nice, but stylized
#

start = time.time()

client = InferenceClient(model="aleksa-codes/flux-ghibsky-illustration",
                         token=Constants.HUGGINGFACE_API_KEY)

print(f"Client created in {time.time()- start} seconds")

response = client.text_to_image(
    prompt="GHIBSKY style, a pond in the middle of a peaceful pine forest with tall trees in the night with fireflies and a full moon lighting the scene",
    height=144,
    width=1024,
    # num_inference_steps=50,
    # model="jbilcke-hf/flux-dev-panorama-lora-2",
    # guidance_scale=7.5,
    # target_size=(1024, 768),
    # seed=42
)

print(f"Response received in {time.time()- start} seconds")

print(response)

# image = Image.open(io.BytesIO(response))

response.save(r"C:\Users\Atvar\Desktop\year2\Team Project\images\ghibsky\scaled_pond_in_forest.jpg")