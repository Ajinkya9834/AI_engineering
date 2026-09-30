from data import question_data
from question_model import Question

q_1 = Question(question_data[0]["text"], question_data[0]["answer"])
print(q_1.text)

# array of obj of questions
question_bank = []

for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    question_bank.append(Question(q_text, q_ans))
