import speech_recognition as sr
import os
import utils as ut
from gtts import gTTS


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        data = ""

        try:
            print("Recognizing...")
            data = r.recognize_google(audio, language='en')
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
