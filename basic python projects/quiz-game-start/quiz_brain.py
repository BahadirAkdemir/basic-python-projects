class QuizBrain():
    def __init__(self, questions):
        self.question_number=0
        self.questions = questions
        self.score=0

    def still_has_question(self):
        if self.question_number < len(self.questions):
            return True
        else:
            return False
    
    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f"{self.question_number} - Q. {current_question.question_text} (True or False)")
        self.check_answer(answer,current_question.question_answer)
    
    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print(f"Correct answer: {correct_answer}")
        print(f"Your score is: {self.score}")

    