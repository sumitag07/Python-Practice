a = [5, 10, 15, 20, 25]

def first_last(a):
    b = [x for x in (a[0],a[-1])]
    print(b)

first_last(a)