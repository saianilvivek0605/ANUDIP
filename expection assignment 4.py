def get_numbers():
    try:
        return float(input("Enter the first number: ")), float(input("Enter the second number: "))
    except ValueError:
        raise TypeError("Error: Both inputs must be numerical values.")

if __name__ == "__main__":
    try:
        num1, num2 = get_numbers()
        print(f"You entered the numbers: {num1} and {num2}")
    except TypeError as e:
        print(e)
