def countdown(n):
    if n < 0:
        print("Blastoff!")
    else:
        print(n)
        n = n - 1
        countdown(n)

countdown(10)
