import audioprocessor as ap


def queryResponder(request_input, answers):
    if(request_input['type'] == 'text_queries'):
        answer = answers[request_input['index']]
        reply = answer.replace(
            "{assistantName}", request_input['assistantName'])
        reply = reply.replace(
            "{userName}", request_input['userName'])
        ap.say(reply)
    else:
        ap.say('Sorry, i didn\'t get you. I still have to learn a lot of things.')
