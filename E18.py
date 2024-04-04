import random
def cowbull(num = input("Guess the number")):
    n = list(str(random.randint(1000,9999)))
    #n = list(str(1235))
    m = list(num)
    b = 0
    c = 0
    for i in range(len(n)):
        for t in range(len(n)):
            if m[i] == n[t] and i ==t:
                c += 1
            elif m[i] == n[t] and i !=t:
                b += 1
    return n,m,b,c
    #print(f"{c} cows and {b} bulls. {n}")

if __name__ == "__main__":
    
    while True:
        n,m,b,c = cowbull()
        if n != m:
            print(f"{c} cows and {b} bulls. {n}")
        else:
            print(f"{c} cows and {b} bulls. {n}")
            break





