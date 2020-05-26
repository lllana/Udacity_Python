# function that creates a flower_dictionary from filename
# def create_flowerdict(filename):
#     flower_dict = {}
#     with open(filename) as f:
#         for line in f:
#             letter = line.split(": ")[0].lower()
#             flower = line.split(": ")[1].strip()
#             flower_dict[letter] = flower
#     return flower_dict
#
# # Main function that prompts for user input, parses out the first letter
# # includes function call for create_flowerdict to create dictionary
# def main():
#     flower_d = create_flowerdict('flowers.txt')
#     full_name = input("Enter your First [space] Last name only: ")
#     first_name = full_name[0].lower()
#     first_letter = first_name[0]
# # print command that prints final input with value from corresponding key in dictionary
#     print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))
#
# main()


# Write your code here

def cast_flower_dict(filename):
    flower_dict = {}
    with open('flower.txt','r') as f:
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
### Data parsingask_name = str(input("Enter your First [space] Last name only: "))ask_name = str(input("Enter your First [space] Last name only: "))
flower_create = cast_flower_dict('flower.txt')

### User's input
ask_name = str(input("Enter your First [space] Last name only: "))

### Programm's output
print("Unique flower name with the first letter: {}".format(contained_letter_flower(ask_name)))
