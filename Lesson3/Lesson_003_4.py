points = 174

prize = None

if points <= 50:
    prize = 'wooden rabbit'
elif points <= 180:
    prize = "wafer-thin mint"
elif points <= 200:
    prize = "a penguin"

if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

# use the truth value of prize to assign result to the correct prize

print(result)
