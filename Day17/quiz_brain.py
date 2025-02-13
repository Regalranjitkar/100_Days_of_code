#Todo-1: Ask question
#Todo-2: Check answer
#Todo-3: Check if we are at the end of the quiz

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        u_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False) : ")
        self.question_number += 1
        self.check_answer(u_answer, current_question.answer)


    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry! that wrong!")

        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is : {self.score}/{self.question_number}.")