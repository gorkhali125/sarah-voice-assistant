import os
import datetime
import audioprocessor as ap


def clearConsole():
    return os.system('clear')


def wishUser(userName):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ap.say("Good Morning " + userName + "! How can i Help you.")

    elif hour >= 12 and hour < 18:
        ap.say("Good Afternoon " + userName + "! How can i Help you.")

    else:
        ap.say("Good Evening " + userName + "! How can i Help you.")
