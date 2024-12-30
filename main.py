from question_model import Question
from quiz_brain import QuizHandler
from data import question_data

question_bank = []
for question in question_data:
  question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizHandler(question_bank)
quiz.run()