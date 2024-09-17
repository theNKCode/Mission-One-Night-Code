from gtts import gTTS
import os 
import pywhatkit
import pywhatkit.sc

Text_to_convert = input("Text to convert:")

language = 'en'

speech = gTTS(text=Text_to_convert, lang= language,slow=False)

speech.save("sagemaker.mp3")

pywhatkit.sendwhats_image('+919510916853','sagemaker.mp3')
