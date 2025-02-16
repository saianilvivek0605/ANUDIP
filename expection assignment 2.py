def get_integer():
    """Prompt the user to input an integer and raise ValueError if input is invalid."""
    while True:
        try:
            # Attempt to convert the input to an integer
            return int(input("Please enter an integer: "))
        except ValueError:
            # Raise a ValueError with a custom message if input is not a valid integer
            print("Error: Invalid input. Please enter a valid integer.")
            
if __name__ == "__main__":
    # Main program to get the user input
    user_integer = get_integer()
    print(f"You entered the integer: {user_integer}")

