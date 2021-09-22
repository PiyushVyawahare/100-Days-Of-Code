from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    obj = Question(questions["question"], questions["correct_answer"])
    question_bank.append(obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nYou've Completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
