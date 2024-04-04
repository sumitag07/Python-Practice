import random
c = ""
b = chr(random.randint(ord('a'),ord('z')))
c += b
d = str(random.randint(0,10))
c += d
print(c)

rand = ""

#print(a)
i = 0
while i <= 4:
    a = random.randint(0,3)
    if a == 1:
        b = chr(random.randint(ord('a'),ord('z')))
                #rand = ''.join(b)
        rand += b
        i += 1
    if a > 1:
        c = str(random.randint(0,9))
                #rand = ''.join(c)
        rand += c
        i += 1
print(rand)
