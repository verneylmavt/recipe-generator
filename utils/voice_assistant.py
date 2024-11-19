# utils/voice_assistant.py
import speech_recognition as sr
import pyttsx3

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            self.speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            self.speak("Sorry, my speech service is down.")
            return ""
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()