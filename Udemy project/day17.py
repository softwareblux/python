# class User:
#     def __init__(self, user_id, username) -> None:
#         self.id = user_id
#         self.username = username
        

# user_1 = User("007", "hei")



# print(user_1.id)

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    qtext = question["question"]
    qanswer = question["correct_answer"]
    newq = Question(qtext= qtext, qanswer=qanswer)
    question_bank.append(newq)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_num}")