distance = float(input("Enter the distance in kilometers: "))
if 1 <= distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = (50 * 8) + (distance - 50) * 10
else:
    fare = (50 * 8) + (50 * 10) + (distance - 100) * 12

print(f"Total fare for {distance} kilometers is Rs. {fare}")
