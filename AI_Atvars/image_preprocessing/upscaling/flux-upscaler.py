import torch
from diffusers.utils import load_image
from diffusers import FluxControlNetModel
from diffusers.pipelines import FluxControlNetPipeline
from PIL import Image


# Does not work

# Load pipeline
controlnet = FluxControlNetModel.from_pretrained(
  "jasperai/Flux.1-dev-Controlnet-Upscaler",
  torch_dtype=torch.bfloat16,
  # use_auth_token=True
)
pipe = FluxControlNetPipeline.from_pretrained(
  "black-forest-labs/FLUX.1-dev",
  controlnet=controlnet,
  torch_dtype=torch.bfloat16,
  add_prefix_space=False
  # revision="refs/pr/1",
  # use_auth_token=True
  
)
# pipe.to("cuda")

control_image = Image.open(r"C:\Users\Atvar\Desktop\year2\Team Project\image_preprocessing\split_images\ghibsky_forest\1.jpg")
# Load a control image
# control_image = load_image(
#   img
# )

w, h = control_image.size

# Upscale x4
control_image = control_image.resize((w * 4, h * 4))

image = pipe(
    prompt="", 
    control_image=control_image,
    controlnet_conditioning_scale=0.6,
    num_inference_steps=28, 
    guidance_scale=3.5,
    height=control_image.size[1],
    width=control_image.size[0]
).images[0]

print(type(image))