from question_model import Question
from data import question_data
from quiz_brain import Brain

# Creating a Question bank
question_bank = []

for i in range(0, len(question_data)):
    new_q = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(new_q)

# initiating an objet from the quiz brain class
new_brain = Brain(question_bank)

while new_brain.score <= len(question_bank):
    new_brain.next_question()



