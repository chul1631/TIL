# 난쟁이 키 리스트에 입력 받음.
height = []

for i in range(9):
    height.append(int(input().split()))

for i in height:
    for j in height:
        if sum(height) - i - j == 100:
            height.remove(i)
            height.remove(j)

height.sort()            
for i in height:
    print(i)

