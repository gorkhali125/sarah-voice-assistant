import time
import audioprocessor as ap
import os

text_responses = [
    'I am fine',
    'Hello',
    'I have no idea. Can you tell me your name please?'
]

# command_responses = [
#     time.ctime(),
# ]

# browser_responses = {
#     'google' : 'https://www.google.com/search?q=',
#     'stackoverflow' : 'https://stackoverflow.com/search?q='
# }

def queryResponder(request_input):
    if(request_input['type'] == 'text_queries'):
        ap.say(text_responses[request_input['index']])
    # elif(request_input['type'] == 'command_queries'):
    #     ap.say(text_responses[request_input['index']])
    # elif(request_input['type'] == 'browser_queries'):
        # spoken_text = spoken_text.split(" ")
        # text = spoken_text[2]
        # ap.say("Hold on David, I will search for " + text + " on .")
        # os.system("google-chrome " + text_responses[request_input['index']] + location +")
    else:
        ap.say('Sorry! I didn\'t get you')