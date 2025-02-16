import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
max_value = max(random_numbers)
min_value = min(random_numbers)
print("Random numbers:", random_numbers)
print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")
