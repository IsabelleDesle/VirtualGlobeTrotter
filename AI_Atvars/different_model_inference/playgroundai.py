from huggingface_hub import InferenceClient
import sys
import os
sys.path.insert(0, os.path.abspath('./AI_Atvars/'))
import Constants

client = InferenceClient("playgroundai/playground-v2.5-1024px-aesthetic", 
                         token=Constants.HUGGINGFACE_API_KEY)

# output is a PIL.Image object
response = client.text_to_image(
    prompt="a panoramic view of a mountain landscape at sunrise with clear skies",
    height=512,
    width=1024,
    num_inference_steps=50,
    # model="jbilcke-hf/flux-dev-panorama-lora-2",
    guidance_scale=7.5,
    # target_size=(1024, 768),
    seed=42
)

response.save(r"./images/playground/mountain_with_clear_skies.jpg")

#
#   This one doesn't work, the Inference API is cold
#