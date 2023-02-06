import string
from translate import Translator
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr
from selenium_web import inflow
from selenium_YT import play_video
from re import search
import datetime

mytext = " "

language = 'en'
accent = 'co.in'
def speak(text):
    myobj1 = gTTS(text=text, lang=language, slow=False, tld=accent)
    myobj1.save("welcome.mp3")
    playsound("welcome.mp3")
    os.remove('welcome.mp3')


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Master !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Master !")
    else:
        speak("Good Evening Master !")
    assname = ("This is Raptor 1 point o. Nice to meet you!, How are you master!")
    speak("I am your Assistant")
    speak(assname)


r = sr.Recognizer()
def hear():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening.......")
        audio = r.listen(source)
        global yourtext
        yourtext = r.recognize_google(audio)
        print(yourtext)
        return yourtext

#wishMe()

while 'exit' or 'bye' or 'tata' not in yourtext: 
    
    yourtext = hear()
    if 'exit' in yourtext or 'Exit' in yourtext or 'bye' in yourtext or 'Bye' in yourtext or 'tata' in yourtext or 'Tata' in yourtext:
        break
    elif 'what about you' in yourtext or 'how are you' in yourtext:
        speak('I am having a good day master!')
        
    elif 'information' in yourtext:
        speak('Information about what?')
        hear()
        print(f'Searching in wikipedia about {yourtext}......')
        assist = inflow()
        txt = assist.get_info(yourtext)
        print(txt)
        speak(txt)
    
    elif 'search' in yourtext or 'Search' in yourtext or 'play' in yourtext or 'Play' in yourtext and ' youtube' in yourtext or ' YouTube' in yourtext or ' Youtube' in yourtext:
        litext = str.split(yourtext)
        if 'search' in litext:
            litext.remove('search')
        elif 'Search' in litext:
            litext.remove('Search')
        elif 'Play' in litext:
            litext.remove('Play')
        elif 'play' in litext:
            litext.remove('play')
        if 'in' in litext:
            litext.remove('in')
        if 'youtube' in litext:
            litext.remove('youtube')
        elif 'YouTube' in litext:
            litext.remove('YouTube')
        elif 'Youtube' in litext:
            litext.remove('Youtube')
        yourtext = ' '.join(litext)
        print(f'Playing your video in YouTube about {yourtext}......')
        speak(f'Playing your video in YouTube about {yourtext}')
        assist = play_video()
        assist.play_vid(yourtext)
        
    
