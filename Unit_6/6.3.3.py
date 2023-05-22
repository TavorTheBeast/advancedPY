import pyttsx3

def read_aloud(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

sentence = "first time i'm using a package in next.py course"
read_aloud(sentence)
