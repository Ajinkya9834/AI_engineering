class QuizBrain:
    def __init__ (self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        current_ans = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(current_ans, question.answer)
    
    def still_has_question(self):
        # if len(self.question_list) > self.question_number:
        #     return True
        # else:
        #     return False
        return len(self.question_list) > self.question_number
    
    def check_answer(self, current_ans, question_ans):
        if current_ans.lower() == question_ans.lower():
            print("You got it right")
            print(f"your correct answer is: {question_ans}")
            self.score += 1
            # print(f"Your score is: {self.score}/{len(self.question_list)}")
        else:
            print("That's wrong")
        print(f"Your score is: {self.score}")
        print("\n")
    
    def final_score(self):
        print("You've completed the quiz")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")