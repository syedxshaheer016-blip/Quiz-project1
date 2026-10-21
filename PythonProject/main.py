import quiz
import file_handler


def show_menu():
    print("\n===== Quiz Management System =====")
    print("1. Start Quiz")
    print("2. View Previous Results")
    print("3. Exit Program")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            # run_quiz() now returns 4 values
            name, score, total, student_answers = quiz.run_quiz()
            file_handler.save_result(name, score, total, student_answers)

        elif choice == "2":
            file_handler.display_results()

        elif choice == "3":
            print("Thank you! Program closed.")
            break

        else:
            print("Invalid choice! Please enter 1, 2 or 3.")
            continue


main()