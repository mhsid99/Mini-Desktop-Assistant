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
import pywhatkit as kit
import pyautogui
import time
import calendar
import pyjokes
import ctypes
from PIL import ImageGrab as ig

engine=px3.init('sapi5') #microsoft's speech recognition API
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

def command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

    try:
        print("Recognizing...")    
        speech=rec.recognize_google(audio, language='en-in')
        print(f"User said: {speech}\n")
    except:
        print("Say that again please...")  
        speak("Say that again please...")
        return "None"
    
    return speech

def wikipedia():
    global speech
    speak('Searching Wikipedia...')
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
    try:
        text=rec.recognize_google(audio)
        print("User: {}".format(text))
        kit.playonyt(text)
        time.sleep(5)
        pyautogui.press('space')
        '''
        url='https://www.youtube.com/results?search_query='
        search_url=url+text
        web.open(search_url)
        '''
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
    
def play_song():
    c=0
    song_dir=r'D:\musica'
    songs=os.listdir(song_dir)
    for i in songs:    
        c+=1
    x=random.randint(0,c)
    print("Here's a song for you")
    speak("Here's a song for you")
    os.startfile(os.path.join(song_dir,songs[x]))

def date():
    day = calendar.day_name[dt.datetime.today().weekday()]
    month_names = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    month = month_names[dt.datetime.now().month-1]
    day_num = str(dt.datetime.now().day)
    date = day_num+'th'+" "+month+" "+ day
    print(date)
    speak(date)

def change_wallpaper():
    c = 0
    wallpaper_dir = r'D:\wallpapers'
    wallpapers = os.listdir(wallpaper_dir)
    for i in wallpapers:
        c += 1
    x = random.randint(0, c)
    path=os.path.join(wallpaper_dir, wallpapers[x])
    print(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

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

    elif 'song' in speech:
        play_song()
        
    elif 'you' in speech or 'yourself' in speech:

        greet=["Hi!", "Hello", "Hey!", "Hey there!", "Kon'nichiwa"]
        greet=greet[random.randint(0, len(greet)-1)]
        print(greet)
        speak("Kon'nichiwa")
        print("My name is PyBot.I was created by Hamza as a mini desktop assistant. I can play youtube videos, search the web, play music, tell date,time and jokes")
        speak("My name is PyBot.I was created by Hamza as a mini desktop assistant. I can play youtube videos, search the web, play music, tell date,time and jokes")
    elif 'date' in speech:
        date()

    elif 'joke' in speech:
        speak("sure")
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif 'wallpaper' in speech:
        change_wallpaper()
        print("Done!")
        speak("Done!")

    elif 'screenshot' in speech:
        image = ig.grab()
        data = image.load()
        image.show()

    elif 'exit' in speech:
        break

        
print("Thank you master! it was a pleasure serving you")
speak("Thank you master! it was a pleasure serving you")


