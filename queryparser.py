import json


def queryParser():
    with open('queries.json') as json_file:
        data = json.load(json_file)
        questions = []
        answers = []
        for singlequery in data['queries']:
            questions.append(singlequery['q'])
            answers.append(singlequery['a'])

    return [questions, answers]
