# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:09:05 2020

@author: Hamza
"""

import pyttsx3 as px3
import speech_recognition as sr
import datetime as dt
import wikipedia as wiki
import webbrowser as web
import os
import random

engine=px3.init('sapi5') #microsoft's speech recognition API
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Master!")   

    else:
        speak("Good Evening Master!")  

    speak("how may I help you")       

def command():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold=1
        audio=rec.listen(source)

    try:
        print("Recognizing...")    
        speech=rec.recognize_google(audio,language='en-in')
        print(f"User said: {speech}\n")

    except Exception:
        print("Say that again please...")  
        return "None"
    
    return speech

def wikipedia():
    global speech
    speak('Searching Wikipedia...')
    speech=speech.replace("wikipedia", "")
    result=wiki.summary(speech,sentences=3)
    speak("According to Wikipedia")
    print(result)
    speak(result)
    
def yt():
    sr.Microphone(device_index=1)
    rec=sr.Recognizer()
    rec.energy_threshold=5000
        
    with sr.Microphone() as source:
        print("What do you want to search?")
        speak("What do you want to search?")
        audio=rec.listen(source)
        text=rec.recognize_google(audio)
        text.lower()
    try:
        text=rec.recognize_google(audio)
        print("User: {}".format(text))
        url='https://www.youtube.com/results?search_query='
        search_url=url+text
        web.open(search_url)
    except:
        print("Can you please say that again?")
        speak("Can you please say that again?")
                        
def google():
    
    sr.Microphone(device_index=1)
    rec=sr.Recognizer()
    rec.energy_threshold=5000

    with sr.Microphone() as source:
        print("what do you want to search")
        speak("what do you want to search")
        audio=rec.listen(source)
    try:
        text=rec.recognize_google(audio)
        print("You said : {}".format(text))
        url='https://www.google.co.in/search?q='
        search_url=url+text
        web.open(search_url)
    except:
        print("Can you please say that again?")
        speak("Can you please say that again?")

def tell_time():
    hour=int(dt.datetime.now().hour)
    minutes=dt.datetime.now().strftime("%M")    
    if hour>12:
        hour=hour-12
        mer='p m'
    else:
        mer='a m'
    hour=str(hour)
    print(hour,':',minutes,mer)    
    speak(f"Sir, the time is")
    speak(hour)
    speak(minutes)
    speak(mer)
    
def show_movie():
    c=0
    movie_dir=r'D:\videos and movies\movies'
    movies=os.listdir(movie_dir)
    for i in movies:    
        print(movies)
        print("\n")
        c+=1
    x=random.randint(0,c)
    print("Here's a random movie for you")
    speak("Here's a random movie for you")
    os.startfile(os.path.join(movie_dir,movies[x]))
    
wish()
while True:
    speech=command().lower()
    if 'wikipedia' in speech:
        wikipedia()

    elif 'youtube' in speech:
        yt()

    elif 'google' in speech:
        google()

    elif 'time' in speech:
        tell_time()   

    elif 'movie' in speech:
        show_movie()

    elif 'job' in speech:
        print("Hey there! I am a mini project desktop assisstant that can surf the web for you and play a random movie.I dont have a name yet")
        speak("hey there! I am a mini project desktop assisstant that can surf the web for you and play a random movie.I dont have a name yet")
        
    elif 'my name' in speech:
        print("Hamza")
        speak("Hamza")
        
    elif 'you' in speech:
        print("hey there! I dont have a name yet")
        speak("hey there! I dont have a name yet")
    
    elif 'exit' in speech:
        break    
        
print("Thank you master! it was a pleasure serving you")
speak("Thank you master! it was a pleasure serving you")