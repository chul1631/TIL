word ='apple'
cnt=0
alp = ['a','e','i', 'o','u']
for i in range(len(word)):
    if word[i] in ['a','e','o','u','i']:
        cnt+=1
print(cnt)

# 풀이

word = 'apple'
# 지금은 인덱스가 필요없어서
# 그냥 char를 받을게
count = 0
for char in word:
    if char =='a' or char =='e'or char =='i' or  char =='o' or char =='u':
        count += 1
print(count)