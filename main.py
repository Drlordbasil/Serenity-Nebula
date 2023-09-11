Sure! Here's an enhanced version of the Python script incorporating the suggested improvements:

```python
# Calculate the factorial of a given number

def calculate_factorial(number):
    """
    Calculate the factorial of a given number.

    Args:
        number (int): Number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.
    """
    if number < 0:
        raise ValueError("Number should be non-negative.")

    if number == 0:
        return 1

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    return factorial


def get_number_from_user():
    """
    Get a non-negative integer input from the user.

    Returns:
        int: The non-negative integer input from the user.
    """
    number = None
    while number is None:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
            number = None

    return number


def main():
    """
    Main function that prompts the user for a number and calculates its factorial.
    """
    number = get_number_from_user()
    
    try:
        factorial = calculate_factorial(number)
        print(f"The factorial of {number} is: {factorial}")
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
```

Here are the changes made in the refactored version:

1. Descriptive variable names have been used throughout the script to enhance readability.
2. The logic has been separated into different functions, `calculate_factorial()` and `get_number_from_user()`, to separate concerns.
3. Comments have been added to explain the purpose and behavior of each function.
4. Error handling has been implemented using a `try-except` block in the `main()` function to handle potential `ValueError` exceptions.
5. The code has been formatted according to the PEP 8 style guide.