class QuizHandler():
  def __init__(self, questions):
    self.question_number = 0
    self.score = 0
    self.question_list = questions

  def response_handler(self, input_string):
    while True:
      response = input(input_string)
      if response.title() == "True" or response.title() == "False":
        return response.title()
      print("I didn't catch that...")

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    question = self.question_list[self.question_number]
    self.question_number += 1
    input_string = f"Q.{self.question_number} {question.text} (True/False): "
    is_correct = self.response_handler(input_string) == question.answer
    if is_correct:
      self.score += 1
    print("You got it right!" if is_correct else "That's wrong.")
    print(f"The correct answer was {question.answer}")
    print(f"Your current score is: {self.score}/{self.question_number}")
    print("\n")
  
  def run(self):
    while self.still_has_questions():
      self.next_question()
    print(f"That's the end of the quiz! Your score was: {self.score}/{len(self.question_list)}")

  