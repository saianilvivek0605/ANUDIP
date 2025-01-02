def calculate_simple_interest(principal, rate, time):
    return(principal * rate * time)/100
principal =200
rate = 5
time = 5
simple_interest = calculate_simple_interest(principal, rate, time)
print(f"the simple interest on Rs. {principal} for {time} years at {rate}% per year is: Rs. {simple_interest}")



