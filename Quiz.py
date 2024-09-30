
questions = {
    "What is the capital of France?": "a",
    "Which planet is known as the Red Planet?": "b",
    "What is the largest ocean on Earth?": "c",
    "Who developed the theory of relativity?": "a",
    "Which element has the chemical symbol 'O'?": "b"
}

options = [
    ["a. Paris", "b. London", "c. Berlin", "d. Rome"],
    ["a. Earth", "b. Mars", "c. Jupiter", "d. Venus"],
    ["a. Atlantic", "b. Indian", "c. Pacific", "d. Arctic"],
    ["a. Albert Einstein", "b. Isaac Newton", "c. Galileo Galilei", "d. Nikola Tesla"],
    ["a. Hydrogen", "b. Oxygen", "c. Nitrogen", "d. Helium"]
]

def check_answer(question, user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")
        return False

def quiz_game():
    score = 0
    for i, (question, correct_answer) in enumerate(questions.items()):
        print(f"Q{i + 1}: {question}")
        for option in options[i]:
            print(option)
        user_answer = input("Your answer (a/b/c/d): ").lower()
        if check_answer(question, user_answer, correct_answer):
            score += 1

    print(f"Your total score is {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!\n")
    quiz_game()
