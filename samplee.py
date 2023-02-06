import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 180)
rate = engine.getProperty('rate')
print(rate)

engine.setProperty('volume', 1.0)
volume = engine.getProperty('volume')
print(volume) 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say("Hello there! My name is Raptor")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

# srch = ['what','about','you']
# count=0
# for i in srch:
#     if i in yourtext:
#         count=count+1
# print(count)
# if count==len(srch):
#     speak('I am having a good day master!')
