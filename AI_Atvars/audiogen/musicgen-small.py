############################################################################################################
# Run inference via the Text-to-Audio (TTA) pipeline. You can infer the MusicGen model via the TTA pipeline in just a few lines of code!
############################################################################################################

# from transformers import pipeline
# import scipy

# synthesiser = pipeline("text-to-audio", "facebook/musicgen-large")
# prompt = "soothing and calming ambient music"
# music = synthesiser(prompt, forward_params={"do_sample": True})

# scipy.io.wavfile.write(f"./outputs/{prompt}.wav", rate=music["sampling_rate"], data=music["audio"])

from transformers import pipeline
import scipy
import torch
import os

# Check if CUDA is available and set device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Create outputs directory if it doesn't exist
os.makedirs("./outputs", exist_ok=True)

# Initialize the pipeline with device specification
synthesiser = pipeline("text-to-audio", "facebook/musicgen-small", device=device)

prompt = "soothing and calming ambient music"
print("Generating music... This might take a while, especially on CPU.")

try:
    music = synthesiser(prompt, 
                       forward_params={"do_sample": True}
                       )
    
    print("Generation complete. Saving file...")
    
    scipy.io.wavfile.write(
        f"./outputs/{prompt}.wav", 
        rate=music["sampling_rate"], 
        data=music["audio"]
    )
    print(f"File saved to ./outputs/{prompt}.wav") # Change this to 'outputs' directory under AI_Atvars/audiogen
    
except Exception as e:
    print(f"An error occurred: {str(e)}")


############################################################################################################
# Run inference via the Transformers modelling code. You can use the processor + generate code to convert text into a mono 32 kHz audio waveform for more fine-grained control.
############################################################################################################

# from transformers import AutoProcessor, MusicgenForConditionalGeneration

# processor = AutoProcessor.from_pretrained("facebook/musicgen-large")
# model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-large")

# inputs = processor(
#     text=["80s pop track with bassy drums and synth", "90s rock song with loud guitars and heavy drums"],
#     padding=True,
#     return_tensors="pt",
# )

# audio_values = model.generate(**inputs, max_new_tokens=256)

