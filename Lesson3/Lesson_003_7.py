names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    new_name = name.lower().replace(' ','_')
    usernames.append(new_name)

print(usernames)
