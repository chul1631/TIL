import sys
sys.stdin = open("BJ_2231.txt")

target = int(input())
 
for i in range(target):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == target:
        print(i)
        break
else:
    print(0)