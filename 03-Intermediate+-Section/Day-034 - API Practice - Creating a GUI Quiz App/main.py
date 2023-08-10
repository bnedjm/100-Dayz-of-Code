from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI


def reformat_data(q_data):
    q_bank = []
    for question in q_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        q_bank.append(new_question)
    return q_bank


question_bank = reformat_data(question_data)
quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
