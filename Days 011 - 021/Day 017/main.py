from question_model import *
from data import *
from quiz_brain import *

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer - NOT MINE"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")