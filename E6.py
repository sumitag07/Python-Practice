word = input("Enter a word")
m = 0
n = int(len(word))
print(word[::-1])
for i in range (n):
    if word[i] == word[n-1-i]:
        #print(word[i],word[n-1-i])
        m += 1
        if m == n:
            print("word is palindrom")