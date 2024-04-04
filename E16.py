import random

def password():
    i = 0
    rand = ""
    while i <=8:
        a = random.randint(0,3)
        if a == 0:
            b = chr(random.randint(ord('a'),ord('z')))
            rand += b
            i += 1
        if a == 2:
            b = chr(random.randint(ord('A'),ord('Z')))
            rand += b
            i += 1
        if a == 1:
            b = str(random.randint(0,9))
            rand += b
            i += 1
    print(rand)
password()

