# importing the gTTS library (google text to speech conversion)
from gtts import gTTS

# importing the os module
import os

# text file to be converted to speech
f = open('text.txt')
x = f.read()

# defining language as English
language = 'en'

# getting the audio file as .wav
audio = gTTS(text=x, lang=language, slow=False)

audio.save("1.wav")
os.system("1.wav")
