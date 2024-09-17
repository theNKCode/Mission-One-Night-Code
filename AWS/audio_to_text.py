import speech_recognition as sr

def listener_text():
    
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
    return text

text = listener_text()
print(text)
