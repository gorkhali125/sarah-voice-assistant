import time

import queryprocessor as qp
import queryresponder as qr
import audioprocessor as ap
import utils as ut

if __name__ == "__main__":

    ut.clearConsole()
    ut.wishUser()
    assistantNAme = ut.setAssistantName()
    userName = ut.setUsername()

    def sarah(spoken_text):
        request_input = qp.queryProcessor(spoken_text)
        if(request_input):
            qr.queryResponder(request_input)

    time.sleep(1)
    while 1:
        spoken_text = ap.listen()
        sarah(spoken_text)
