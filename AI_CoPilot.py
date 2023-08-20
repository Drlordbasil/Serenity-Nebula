Here is an AI chatbot program that helps the user run the provided main.py script locally on their PC:

```python
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
```

To run this chatbot, simply save the code in a Python file (e.g., `chatbot.py`) and execute it using the command `python chatbot.py` in your command line interface. The chatbot will prompt you to enter "yes" or "no" to run the main program.