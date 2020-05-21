num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_num = []

for numbers in num_list:
    if numbers % 2 == 1 and len(odd_num) < 5:
        odd_num.append(numbers)

print(odd_num)
