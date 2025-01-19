import IPython
import soundfile as sf
from tango import Tango

# TANGO can generate realistic audios including human sounds, animal sounds, natural and artificial sounds and sound effects from textual prompts.

# Cannot run unfortunately, because I'm not able to install the Tango library on my local machine.
tango = Tango("declare-lab/tango")

prompt = "A soothing soundscape of natural sounds heard in an amazon rainforest"
audio = tango.generate(prompt)
sf.write(f"{prompt}.wav", audio, samplerate=16000)
IPython.display.Audio(data=audio, rate=16000)
