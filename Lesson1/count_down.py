n = 5

def countdown():
    global n
    if n < 0:
        print("Blastoff!")
    else:
        print(n)
        n = n - 1
        countdown()

countdown()
