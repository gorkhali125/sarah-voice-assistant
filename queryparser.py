import json


def queryParser():
    with open('queries.json') as json_file:
        data = json.load(json_file)
        questions = []
        answers = []
        for p in data['queries']:
            questions.append(p['q'])
            answers.append(p['a'])

    return [questions, answers]
