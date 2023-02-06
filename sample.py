from translate import Translator
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr

mytext = "Hello Aryan Dev! My name is Raptor. Nice to meet you!"
language = 'en'
accent = 'co.in'
myobj1 = gTTS(text=mytext, lang=language, slow=False, tld=accent)
myobj1.save("welcome1.mp3")
playsound("welcome1.mp3")
os.remove('welcome1.mp3')

translator = Translator(to_lang='hi')
translation = translator.translate(mytext)
language = 'hi'
myobj2 = gTTS(text=translation, lang=language, slow=False, tld=accent)
print (translation)
myobj2.save("welcome2.mp3")
playsound("welcome2.mp3")
os.remove('welcome2.mp3')
