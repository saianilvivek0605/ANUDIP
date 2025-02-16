def find_duplicates(numbers):
    duplicates = []
    seen = []
    for num in numbers:  # Corrected from 'number' to 'numbers'
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.append(num)
    return duplicates

numbers = [1, 2, 3, 4, 5, 1, 2, 6]
duplicates = find_duplicates(numbers)  # Corrected function name
print("duplicate values:", duplicates)
