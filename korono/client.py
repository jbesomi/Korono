import requests
import json


def get_answers_json(q):
    url = "http://127.0.0.1:5000/ask/{}/".format(q)
    response = requests.post(url)
    return json.loads(response.text)


def get_answers(q):
    answers = get_answers_json(q)
    results = answers["results"]
    for r in results:
        if r["answer"].strip() is not "":
            print(r["answer"])
