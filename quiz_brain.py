# TODO: Asking Questions
# TODO: Checking if correct
# TODO: Checking if its the end

class Brain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_bank = q_bank
        self.score = 0
    def next_question(self):

        answer = (input(f"Q.{self.question_number}: {self.question_bank[self.question_number].Question} (True / False) "))
        if answer.title() == self.question_bank[self.question_number].Answer:
            print("Correct")
            self.score += 1
        else:
            print(f"Wrong Answer! The Correct Answer is { self.question_bank[self.question_number].Answer}")
        self.question_number += 1
