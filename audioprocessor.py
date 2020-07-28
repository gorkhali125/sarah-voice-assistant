import speech_recognition as sr
import os
from gtts import gTTS


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.record(source, 5)
        data = ""
        try:
            data = r.recognize_google(audio)
            print("You said: " + data.lower())
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

    return data.lower()


def say(audioString):
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")