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
    ap.say("What should i call you")
    userName = ap.listen()
    ap.say("Welcome " + userName + ". How can i Help you.")
    return userName


def setAssistantName():
    ap.say("What name do you give me sir")
    assistantName = ap.listen()
    ap.say("Thanks for the lovely name")
    return assistantName
