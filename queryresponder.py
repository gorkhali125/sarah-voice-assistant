import audioprocessor as ap

text_responses = [
    'I am fine',
    'Hello',
    'I have no idea. Can you tell me your name please?'
]


def queryResponder(request_input):
    if(request_input['type'] == 'text_queries'):
        ap.say(text_responses[request_input['index']])
    else:
        ap.say('Sorry! I didn\'t get you')
