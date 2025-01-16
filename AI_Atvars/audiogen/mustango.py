import IPython
import soundfile as sf
from mustango import Mustango

model = Mustango("declare-lab/mustango")

prompt = "A background ambient track to be played in a museum or art exibition"

music = model.generate(prompt)
sf.write(f"{prompt}.wav", music, samplerate=16000)
IPython.display.Audio(data=music, rate=16000)
