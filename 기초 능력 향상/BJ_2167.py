import sys

sys.stdin = open("BJ_2167.txt")

N, M = map(int, input().split())

arr = []
answer = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum = 0
    for a in range(i - 1, x):
        for k in range(j - 1, y):
            sum += arr[a][k]
    answer.append(sum)


for prt in answer:
    print(prt)
