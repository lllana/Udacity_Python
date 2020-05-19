points = 174

if points <= 50:
    result = "wooden rabbit"
if points <= 180:
    result = "wafer-thin mint!"
if points <= 200:
    result = "a penguin!"
print("Congratulations! You won a {}!".format(result))

if points <= 150:
    print("Oh dear, no prize this time.")
