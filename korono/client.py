import requests


def ask_question(q):
    url = "http://127.0.0.1:5000/ask/{}/".format(q)
    response = requests.post(url)
    return response.text
