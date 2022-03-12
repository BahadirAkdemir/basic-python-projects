from data import question_data
from question_model import Question

quest_list = []

for question in question_data:
    quest_list.append(Question(question['question'],question['correct_answer']))
print(len(quest_list))
from quiz_brain import QuizBrain
quiz_brain = QuizBrain(quest_list)

while quiz_brain.still_has_question():
    quiz_brain.next_question()