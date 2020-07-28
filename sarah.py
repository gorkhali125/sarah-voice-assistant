import time

import queryprocessor as qp
import queryresponder as qr
import audioprocessor as ap

if __name__ == "__main__":

    def sarah(spoken_text):        
        request_input = qp.queryProcessor(spoken_text)
        if(request_input):
            qr.queryResponder(request_input)


    ap.say("Hi David, what can I do for you?")
    while 1:
        spoken_text = ap.listen()
        sarah(spoken_text)