num = int(input("Enter a number"))
check = int(input("Enter a number"))

if num%check == 0:
    print(f"{check} devides {num} evenly")
else:
    print(f"{check} does not devide {num} evenly")