import time

import os
import queryprocessor as qp
import queryresponder as qr
import audioprocessor as ap
import utils as ut
import queryparser as qep
import subprocess

if __name__ == "__main__":

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
        sarah(spoken_text)
