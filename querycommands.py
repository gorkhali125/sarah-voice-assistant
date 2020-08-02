import os
import time
import audioprocessor as ap
import pyjokes
import wikipedia


def queryCommands(text):
    if(text == "powerpoint"):
        os.system("libreoffice --draw")

    elif(text == "excel"):
        os.system("libreoffice --calc")

    elif(text == "writer"):
        os.system("libreoffice --writer")

    elif(text == "time"):
        ap.say(time.ctime())

    elif(text == "vs code"):
        os.system("code")

    elif(text == "joke"):
        ap.say(pyjokes.get_joke())

    elif("wikipedia" in text):
        query = text.replace("wikipedia", "").strip()
        if(query == ""):
            ap.say("Sorry! I cannot find anything to search for...")
        else:
            results = wikipedia.summary(query, sentences=1)
            ap.say("According to Wikipedia...")
            print(results)
            ap.say(results)

    elif(text == "shutdown system"):
        confirm = ap.listen()
        if("yes" in confirm):
            os.system("shutdown -h +1")
            ap.say("Shutting down in 1 minute")
        else:
            ap.say("Aborting Shutdown..")

    elif(text == "restart system"):
        confirm = ap.listen()
        if("yes" in confirm):
            os.system("shutdown -r +1")
            ap.say("Restarting in 1 minute")
        else:
            ap.say("Aborting Restart..")
            
    elif(text in ["cancel shutdown", "cancel restart"]):
        os.system("shutdown -c")