num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_num = []

for numbers in num_list:
    if numbers % 2 == 1 and len(odd_num) < 5:
        odd_num.append(numbers)


print("The sum of the odd numbers added is: {}.". format(format(sum(odd_num))))
print("The numbers of odd numbers added are: {}.".format(len(odd_num)))

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] %2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}.".format(count_odd))
print ("The sum of the odd numbers added is: {}.".format(list_sum))
