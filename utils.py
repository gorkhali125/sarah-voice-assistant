import os
import datetime
import audioprocessor as ap


def clearConsole():
    return os.system('clear')


def wishUser(userName):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ap.say("Good Morning " + userName + "! What can I do for you?")

    elif hour >= 12 and hour < 18:
        ap.say("Good Afternoon " + userName + "! What can I do for you?")

    else:
        ap.say("Good Evening " + userName + "! What can I do for you?")
