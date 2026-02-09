def quiz_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
            "answer": "B"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
            "answer": "C"
        },
        {
            "question": "What is 5 + 3?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "D"
        }
    ]

    score = 0

    print("=== Welcome to the Quiz Game ===\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong ❌ Correct answer is {q['answer']}\n")

    print("Quiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
