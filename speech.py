import speech_recognition as sr
import time


r =sr.Recognizer()
with sr.Microphone() as source:
    
        print("Pode falar ... ")
        audio = r.listen(source)
        
    print(r.recognize_google(audio))
    
   
