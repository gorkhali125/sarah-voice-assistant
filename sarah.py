import time

import os
import queryprocessor as qp
import queryresponder as qr
import audioprocessor as ap
import utils as ut
import queryparser as qep
import subprocess

if __name__ == "__main__":

    started = False
    ut.clearConsole()
    assistantName = "Sarah"
    userName = subprocess.check_output("whoami", shell=True).decode("utf-8")
    ut.wishUser(userName)

    [questions, answers] = qep.queryParser()

    def sarah(spoken_text):
        request_input = qp.queryProcessor(spoken_text, questions)
        if(request_input):
            request_input['userName'] = userName
            request_input['assistantName'] = assistantName
            qr.queryResponder(request_input, answers)

    time.sleep(1)
    while 1:
        spoken_text = ap.listen()
        if(spoken_text == 'start listening'):
            ap.say('Ready for your command sire!')
            started = True

        if(spoken_text == 'stop listening'):
            if(started):
                ap.say('Talk to you later sire!')
            started = False

        if(started and spoken_text != "start listening"):
            sarah(spoken_text)
