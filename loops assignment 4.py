total_sum = 0
while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total_sum += num
print(f"The sum of all entered numbers is {total_sum}")
