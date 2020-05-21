start_num = 0 #provide some start number
end_num = 90 #provide some end number that you stop when you hit
count_by = 10 #provide some number to count by

# write a while loop that uses break_num as the ongoing number to
break_num = start_num
while break_num < end_num:
    break_num += count_by
#   check against end_num

print(break_num)

start_num = 90 #provide some start number
end_num = 190 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by


# write a condition to check that end_num is larger than start_num before looping
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
        result = break_num
# write a while loop that uses break_num as the ongoing number to
#   check against end_num

print(result)

limit = 40
a = 1

# write your while loop here

while (a + 1)**2 < limit:
    a += 1
nearest_square = a**2

print(nearest_square)
