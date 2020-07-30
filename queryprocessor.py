text_queries = [
    'how are you',
    'hello',
    'my name'
]

# command_queries = [
#     'time',
# ]

# browser_queries = [
#     'google',
#     'stackoverflow'
# ]


def generateRequestDict(request_index, request_type, spoken_text):
    request_input = dict()
    request_input['index'] = request_index
    request_input['type'] = request_type
    request_input['text'] = spoken_text
    return request_input


def queryProcessor(spoken_text):
    if(spoken_text in text_queries):
        return generateRequestDict(text_queries.index(spoken_text), 'text_queries', spoken_text)
    # elif(spoken_text in command_queries):
    #     return generateRequestDict(command_queries.index(spoken_text), 'command_queries', spoken_text)
    # elif(spoken_text in browser_queries):
    #     return generateRequestDict(browser_queries.index(spoken_text), 'browser_queries', spoken_text)
    elif(len(spoken_text) > 0):
        return generateRequestDict(0, 'not_found', spoken_text)
