from korono import client

q = "What is coronavirus?"
answer = client.ask_question(q)
print(answer)
