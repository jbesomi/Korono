from korono import client

q = "What is coronavirus?"
answers = client.get_answers(q)
print(answers)
