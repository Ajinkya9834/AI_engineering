from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# array of obj of questions
question_bank = []

for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    question_bank.append(Question(q_text, q_ans))

question_obj = QuizBrain(question_bank)
# question_obj.next_question()
# question_obj.still_has_question()

while question_obj.still_has_question():
    question_obj.next_question()