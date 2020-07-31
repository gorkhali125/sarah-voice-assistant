import os
import time
import audioprocessor as ap
import pyjokes
import wikipedia


def checkCommands(text):
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
        os.system("shutdown -h now")
        exit()

def queryResponder(request_input, answers):
    if(request_input['type'] == 'text_queries'):
        answer = answers[request_input['index']]
        reply = answer.replace(
            "{assistantName}", request_input['assistantName'])
        reply = reply.replace(
            "{userName}", request_input['userName'])
        ap.say(reply)
        checkCommands(request_input['text'])

    elif(request_input['type'] == 'command_queries'):
        answer = answers[request_input['index']]
        ap.say(answer)
        checkCommands(request_input['text'])

    else:
        ap.say('Sorry, i didn\'t get you.')
