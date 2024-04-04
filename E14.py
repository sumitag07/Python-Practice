import random
#a = random.sample(range(99),6)
a = [1,1,3,5,234,3,23,54,98]
def list_(a):
    b = set(a)
    print(list(b))

def list_2(a):
    c = []
    for x in a:
        if x not in c:
            c.append(x)
    print(c)
list_(a)
list_2(a)