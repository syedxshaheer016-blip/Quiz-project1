import datetime

FILE_NAME = "results.txt"


def save_result(name, score, total, student_answers):

    try:

        now = datetime.datetime.now()
        time_stamp = now.strftime("%d-%m-%Y %H:%M:%S")

        with open(FILE_NAME, "a") as file:
            # Header for this attempt
            file.write("========================================\n")
            file.write("Student : " + name + "\n")
            file.write("Date    : " + time_stamp + "\n")
            file.write("----------------------------------------\n")


            for item in student_answers:
                file.write("Question       : " + item["question"] + "\n")
                file.write("Student Answer : " + item["given"] + "\n")
                file.write("Correct Answer : " + item["correct"] + "\n")
                file.write("Result         : " + item["result"] + "\n")
                file.write("----------------------------------------\n")


            file.write("Final Score : " + str(score) + "/" + str(total) + "\n")
            file.write("========================================\n\n")

        print("Result saved in", FILE_NAME)
    except Exception as error:
        print("Sorry, result could not be saved. Error:", error)


def display_results():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No results file found. Please play the quiz first.")
        return
    except Exception as error:
        print("Error while reading the file:", error)
        return

    if len(lines) == 0:
        print("Results file is empty. No records yet.")
        return

    print("\n----- Previous Results -----")
    for line in lines:
        print(line.rstrip())
    print("----------------------------")