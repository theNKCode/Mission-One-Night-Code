from gtts import gTTS
import os 

Text_to_convert = input("Text to convert:")

language = 'en'

speech = gTTS(text=Text_to_convert, lang= language,slow=False)

speech.save("sagemaker.mp3")

os.system("start sagemaker.mp3")