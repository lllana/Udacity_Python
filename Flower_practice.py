# Write your code here

def cast_flower_dict(filename):
    flower_dict = {}
    with open('flowers.txt','r') as f:
        for line in f:
            line_data = line.split(":")

            letter = line_data[0]
            name = line_data[1].strip("\n").strip()

            flower_dict[letter] = name
    return flower_dict

def contained_letter_flower(ask_name):
    letter = ask_name[:1]
    flower = flower_create.get(letter)
    return flower

### Data parsing
flower_create = cast_flower_dict('flower.txt')

### User's input
ask_name = str(input("Enter your First [space] Last name only: "))

### Programm's output
print("Unique flower name with the first letter: {}".format(contained_letter_flower(ask_name)))
