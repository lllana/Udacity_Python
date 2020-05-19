names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    new_name = name.lower().replace(' ','_')
    usernames.append(new_name)

print(usernames)

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ', '_')
print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in tokens:
    if i[0]=='<' and i[-1]=='>':
        count +=1
print(count)
