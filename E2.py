num = int(input("Enter a Number"))

if num%2 == 0:
    print("number is even")
    if num%4 == 0:
        print("number is multiple of 4")
else:
    print("number is odd")