def generateRequestDict(request_index, request_type, spoken_text):
    request_input = dict()
    request_input['index'] = request_index
    request_input['type'] = request_type
    request_input['text'] = spoken_text
    return request_input


def queryProcessor(spoken_text, questions):
    if(spoken_text in questions):
        return generateRequestDict(questions.index(spoken_text), 'text_queries', spoken_text)
    elif(len(spoken_text) > 0):
        return generateRequestDict(0, 'not_found', spoken_text)
