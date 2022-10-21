# https://www.acmicpc.net/problem/1769
import sys

sys.stdin = open("BJ_1769.txt","r")

n = list(map(int,str(input())))

i = 0 
while True:
    if len(n) == 1:
        result = n[0]
        break
    i += 1
    
    result = 0
    for j in n:
        result += j
        
    if result < 10:
        break
    else:
        n = list(map(int,str(result)))
    
if result == 3 or result == 6 or result == 9:
    print(i)
    print('YES')

else:
    print(i)
    print('NO')