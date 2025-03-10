from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for i in question_data:
    questions_bank.append(Question(i["text"], i["answer"]))

# for i in questions_bank:
#     print(i.question_text)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()
