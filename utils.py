import os
import datetime
import audioprocessor as ap


def clearConsole():
    return os.system('clear')


def wishUser():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ap.say("Good Morning!")

    elif hour >= 12 and hour < 18:
        ap.say("Good Afternoon!")

    else:
        ap.say("Good Evening!")


def setUsername():
    ap.say("What should i call you sir")
    uname = ap.listen()
    ap.say("Welcome " + uname + ". How can i Help you.")


def setAssistantName():
    ap.say("What name do you give me sir")
    assistantName = ap.listen()
    ap.say("Thanks for the lovely name")
    return assistantName
