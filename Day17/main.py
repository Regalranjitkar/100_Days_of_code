from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

i=0

for question in question_data:
    question = Question(question["question"], question["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Congratulations! You have completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")