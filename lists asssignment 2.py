my_list = [4, 2, 5, 1, 6, 9, 7, 2]

min_num = my_list[0]
max_num = my_list[0]

for num in my_list:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num

print(f'min num from the list = {min_num}')
print(f'max num from the list = {max_num}')
