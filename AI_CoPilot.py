
import subprocess


def run_program():
    try:
        subprocess.run(["python", "main.py"], check=True)
        print("Program executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing program: {e}")


def main():
    print("Welcome to the AI chatbot!")
    print("This chatbot will help you run the program locally on your PC.")
    print("Are you ready to run the program? (yes/no)")

    while True:
        choice = input("> ")

        if choice.lower() == "yes":
            run_program()
            break
        elif choice.lower() == "no":
            print("Okay, let me know when you're ready.")
            break
        else:
            print("Invalid choice, please try again.")
            continue


if __name__ == "__main__":
    main()
