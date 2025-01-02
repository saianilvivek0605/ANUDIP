num = int(input("Enter a number to find its factorial: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"Factorial of {num} is {factorial}")
