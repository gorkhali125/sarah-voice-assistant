def generateRequestDict(request_index, request_type, spoken_text):
    request_input = dict()
    request_input['index'] = request_index
    request_input['type'] = request_type
    request_input['text'] = spoken_text
    return request_input


def queryProcessor(spoken_text, questions):
    if(spoken_text in questions):
        return generateRequestDict(questions.index(spoken_text), 'text_queries', spoken_text)

    elif 'powerpoint' in spoken_text:
        return generateRequestDict(questions.index("powerpoint"), 'command_queries', "powerpoint")
    
    elif 'excel' in spoken_text:
        return generateRequestDict(questions.index("calc"), 'command_queries', "excel")
    
    elif 'writer' in spoken_text:
        return generateRequestDict(questions.index("writer"), 'command_queries', "writer")

    elif 'time' in spoken_text:
        return generateRequestDict(questions.index("time"), 'command_queries', "time")
    
    elif 'vs code' in spoken_text:
        return generateRequestDict(questions.index("vs code"), 'command_queries', "vs code")
    
    elif 'joke' in spoken_text:
        return generateRequestDict(questions.index("joke"), 'command_queries', "joke")

    elif(len(spoken_text) > 0):
        return generateRequestDict(0, 'not_found', spoken_text)
