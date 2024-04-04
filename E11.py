def get_prime():
    num = int(input("Enter a number"))
    test = False
    for i in range(2,10):
        if num != i and num%i == 0:
            test = True
    if test == True:
        print("Numer is Not a prime number")
    else:
        print("Number is a prime number")

a = get_prime()