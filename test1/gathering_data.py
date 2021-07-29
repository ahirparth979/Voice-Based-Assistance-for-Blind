'''
Created on Sep 9, 2020

@author: Parth Ahir
'''

import speech_recognition as sr
from gtts import gTTS
import os
import smtplib
import pyttsx3

k = pyttsx3.init()
k.setProperty('volume', 1)
k.setProperty('rate', 125)
k.setProperty('voice', k.getProperty('voices')[3].id)

r = sr.Recognizer()

def tts(text):
    k.say(text)
    k.runAndWait()
    
def stt():
    flag = True
    while flag:
        with sr.Microphone() as source:
            #print("Please wait. Calibrating microphone...") 
            r.adjust_for_ambient_noise(source, duration = 2)
            #r.dynamic_energy_threshold = True
            tts('Now speak')
            audio = r.listen(source)
        try:
            text = (r.recognize_google(audio, language = 'en-IN'))
            return text
            flag = False
        except:
            tts('something went wrong, please try again')
            flag = True
            
tts('Welcome to Voice based assistance for sending email')

tts('Please speak your email when prompted')
user_email = stt()
user_email = user_email.replace(" ","").lower()
print(user_email)

tts('Please speak your password when prompted')
user_pass = stt()
user_pass = user_pass.replace(" ","").lower()
print(user_pass)

tts('Please speak the content of the mail when prompted')
message = stt()
print(message)

tts("Please speak the receiver's email address when prompted")
receiver_email = stt()
receiver_email = receiver_email.replace(" ","").lower()
print(receiver_email)
