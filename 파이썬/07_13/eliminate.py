word = 'apple'
result = word
for i in word:
    if i in 'a':
        result = result.replace(i,'')
print(result)