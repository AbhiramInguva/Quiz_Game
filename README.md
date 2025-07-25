# 🧠 Python Quiz Game

A sleek command-line True/False quiz application written in Python.

## ✨ Overview

This application presents users with True/False questions from various categories and tracks their score. It demonstrates object-oriented programming principles through a simple architecture that separates data, models, and game logic.

## 📁 Files

### question_model.py

Defines the Question class that stores questions and answers.

```python
class Question:
    def __init__(self, question, answer):
        self.Question = question
        self.Answer = answer
```

### quiz_brain.py

Contains the Brain class that manages the quiz flow.

```python
class Brain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_bank = q_bank
        self.score = 0
        
    def next_question(self):
        current_question = self.question_bank[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.Question} (True/False): ")
        self.check_answer(answer, current_question.Answer)
        self.question_number += 1
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Wrong! The correct answer is {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number + 1}\n")
```

### data.py

Contains the quiz questions database with 50 True/False questions across various categories.

```python
# Sample of the question_data structure
question_data = [
    {
        "category": "General Knowledge",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The Great Wall of China is visible from the moon.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    # More questions...
]
```

### main.py

The entry point that initializes and runs the quiz.

```python
from question_model import Question
from data import question_data
from quiz_brain import Brain

def main():
    # Create question bank
    question_bank = []
    for question in question_data:
        new_question = Question(question["question"], question["correct_answer"])
        question_bank.append(new_question)
    
    # Initialize quiz
    quiz = Brain(question_bank)
    
    # Run quiz until questions are exhausted
    while quiz.question_number < len(question_bank):
        quiz.next_question()
    
    # Show final score
    print("You've completed the quiz!")
    print(f"Your final score: {quiz.score}/{len(question_bank)}")

if __name__ == "__main__":
    main()
```

## 🚀 Installation

No special installation required beyond Python 3.6+.

## 🎮 Usage

Run the application with:

```
python main.py
```

Answer each question with "True" or "False" when prompted.

## 📚 Categories

Questions cover diverse topics including:
- 🧠 General Knowledge
- 🎬 Entertainment (Video Games, Film, TV)
- 🔬 Science & Nature
- 📜 History
- 🗺️ Geography
- 🏛️ Politics

## 🤝 Contributing

Contributions welcome! Possible improvements:
- Add more questions to the database
- Implement category selection
- Add difficulty levels
- Create a GUI version
- Add a timer for each question

## 📄 License

MIT License
