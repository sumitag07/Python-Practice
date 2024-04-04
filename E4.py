num = int(input("enter a number"))
x = []
for i in range(num+1):
    if i>0 and num%(i) ==0:
        x.append(i)
print(x)