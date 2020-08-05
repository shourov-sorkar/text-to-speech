from gtts import gTTS
import os
tts = gTTS(text='Hello shourov', lang='en')
tts.save("speech.mp3")
os.system("speech.mp3")
