import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
 
for case in range(1, T + 1):
    num = int(input())
    cnt = 0
    num_list = list(map(int, input().split()))
    avg = sum(num_list)/len(num_list)
    for i in range(num) :
        if num_list[i] <= avg :
            cnt = cnt + 1
    print('#', end='')
    print(case, cnt)