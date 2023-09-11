import subprocess
Here's an optimized version of the script:

```python


def run_program():
    try:
        subprocess.check_call(["python", "main.py"])
        print("Program executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing program: {e}")


def main():
    print("Welcome to the AI chatbot!")
    print("This chatbot will help you run the program locally on your PC.")
    print("Are you ready to run the program? (yes/no)")

    while True:
        choice = input("> ").lower()

        if choice == "yes":
            run_program()
            break
        elif choice == "no":
            print("Okay, let me know when you're ready.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
```

Changes made:
1. Instead of using `subprocess.run`, we can use `subprocess.check_call` which raises a `CalledProcessError` if the subprocess returns a non-zero exit status.
2. Applied `.lower()` method to the `choice` input to make the comparison case-insensitive.
3. Removed the unnecessary `continue ` statement in the while loop.
4. Removed the unnecessary `print` statement after the `input` statement in the while loop.
