import random

n = random.randint(1,9)
exit = ""
r = 0
while exit != "exit":
    num = int(input("Guess the number"))
    if num<n:
        print("You guessed low")
        r += 1
    elif num>n:
        print("You guessed high")
        r += 1
    else:
        print("You guessed it correct")
        r += 1
        print(f"you took {r} tries")
        r = 0
    exit = input("Retry or exit")



