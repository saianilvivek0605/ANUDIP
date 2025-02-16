def divide_numbers(num1, num2):
    # Function to divide two numbers and handle division by zero
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

if __name__ == "__main__":
    # Prompt the user to enter two numbers separated by a space
    num1, num2 = map(float, input("Enter two numbers separated by space: ").split())
    # Print the result of the division
    print(f"Result of division: {divide_numbers(num1, num2)}")
