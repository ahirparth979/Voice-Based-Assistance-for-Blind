'''
Created on Oct 23, 2020

@author: Parth Ahir
'''

import speech_recognition as sr
import smtplib
import pyttsx3
import sqlite3

k = pyttsx3.init()
k.setProperty('volume', 1)
k.setProperty('rate', 125)
k.setProperty('voice', k.getProperty('voices')[3].id)

r = sr.Recognizer()
#r.energy_threshold = 10000
user_email = ''
user_list = []
receiver_email = ''
receiver_list = []
password = ''

def tts(text):
    k.say(text)
    k.runAndWait()
    
def stt(choice):
    flag = True
    while flag:
        with sr.Microphone() as source:
            #print("Please wait. Calibrating microphone...") 
            r.adjust_for_ambient_noise(source, duration = 2)
            #r.dynamic_energy_threshold = True
            tts('Now speak your' + choice)
            audio = r.listen(source)
        try:
            text = (r.recognize_google(audio, language = 'en-US'))
            return text
            flag = False
        except:
            tts('something went wrong, please try again')
            flag = True

def view_user():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT email FROM user")
    column = cur.fetchall()
    conn.close()
    return column

def view_pin():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT pin FROM user WHERE email == ?",(user_email,))
    pin = cur.fetchall()
    conn.close()
    return pin

def view_password():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT password FROM user WHERE email == ?",(user_email,))
    password = cur.fetchall()
    conn.close()
    return password

def view_receiver():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT email FROM receiver")
    column = cur.fetchall()
    conn.close()
    return column

def login():
    global user_email
    global password
    
    
    flag = True
    tts('select the account number to login')
    for emails in view_user():
        user_list.append(emails[0])
    for index in range(len(user_list)):
        tts(str(index+1))
        tts(user_list[index])

    while flag:
         
        email_choice = stt('choice').lower()
        #print(email_choice)
    
        if email_choice == '1' or email_choice == 'one' or email_choice == 'van':
            flag = False
            user_email = user_list[0]
        elif email_choice == '2' or email_choice == 'two' or email_choice == 'tu':
            flag = False
            user_email = user_list[1]
        else:
            tts('Try Again')
    
    #user_email = view_user()[0][0]
    print('user email : ' + user_email)
    tts(' Hello ' + user_email)
    tts('4-digit security pin')
    pin = int(stt('pin'))
    #print('4-digit security pin : ' + str(pin))
    if(pin == view_pin()[0][0]):
        password = view_password()[0][0]

def receiver_email():
    global receiver_email
    flag = True
    tts("select the receiver's email")
    for emails in view_receiver():
        receiver_list.append(emails[0])
    for index in range(len(receiver_list)):
        tts(str(index+1))
        tts(receiver_list[index])
    
    while flag:
         
        email_choice = stt('choice').lower()
        #print(email_choice)
    
        if email_choice == '1' or email_choice == 'one' or email_choice == 'van':
            flag = False
            receiver_email = receiver_list[0]
        elif email_choice == '2' or email_choice == 'two' or email_choice == 'tu':
            flag = False
            receiver_email = receiver_list[1]
        else:
            tts('Try Again')
    print("receiver's email : " + receiver_email)
    tts('Email will be sent to ' + receiver_email)

#__main__

print('Welcome to Voice based assistance for sending email')
tts('Welcome to Voice based assistance for sending email')

login()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(user_email, password)
print('Successfully logged in')
tts('successfully logged in')

receiver_email()

message = stt('message')
print("Email body : " + message)

s.sendmail(user_email, receiver_email, message)
tts('email sent successfully to ' + receiver_email)
s.quit()


