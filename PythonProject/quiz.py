questions = [
    {
        "question": "1. What is the capital of Pakistan?",
        "options": ["A. Karachi", "B. Lahore", "C. Islamabad", "D. Peshawar"],
        "answer": "C"
    },
    {
        "question": "2. Which language are we using for this project?",
        "options": ["A. Java", "B. Python", "C. C++", "D. PHP"],
        "answer": "B"
    },
    {
        "question": "3. What is 5 + 7 ?",
        "options": ["A. 10", "B. 11", "C. 13", "D. 12"],
        "answer": "D"
    },
    {
        "question": "4. Which keyword is used to exit a loop?",
        "options": ["A. stop", "B. break", "C. exit", "D. end"],
        "answer": "B"
    },
    {
        "question": "5. Which function is used to open a file in Python?",
        "options": ["A. open()", "B. file()", "C. read()", "D. load()"],
        "answer": "A"
    }
]


def calculate_score(correct_answers, total_questions):
    score = correct_answers
    return score


def run_quiz():

    name = ""
    while True:
        name = input("Enter your name: ").strip()
        if name == "":
            print("Name cannot be empty! Please try again.")
            continue
        break

    correct_answers = 0
    total_questions = len(questions)

    student_answers = []


    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer not in ["A", "B", "C", "D"]:
                print("Invalid answer! Please enter A, B, C or D.")
                continue
            break


        if answer == q["answer"]:
            print("Correct!")
            correct_answers = correct_answers + 1
            result = "Correct"
        else:
            print("Wrong! The correct answer is", q["answer"])
            result = "Wrong"


        student_answers.append({
            "question": q["question"],
            "given": answer,
            "correct": q["answer"],
            "result": result
        })
    score = calculate_score(correct_answers, total_questions)

    print("\n----- Quiz Finished -----")
    print("Student :", name)
    print("Score   :", score, "out of", total_questions)

    return name, score, total_questions, student_answers