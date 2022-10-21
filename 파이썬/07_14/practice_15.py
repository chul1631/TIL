word = 'banana'
for i in range(len(word)):
    if word[i] =='a':
        break
    else:
        i = -1
print(i)

x = "HappyHacking"
y = list(x)
con = 0
for i in range(len(y)):
    if y[i] == 'a':
        con += 1
        print(i,end=' ')


