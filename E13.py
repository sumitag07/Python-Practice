

def fibonacci():
    a = int(input("Enter a number"))
    n = 1
    m = 0
    p = 0
    for i in range(a):
        print(n)
        m = n
        n = p+n
        p = m

fibonacci()