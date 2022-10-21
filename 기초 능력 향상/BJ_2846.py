import sys

sys.stdin = open("BJ_2846.txt")

n = int(input())
li = list(map(int, input().split()))
a = 0
result = []
for i in range(n - 1):
    if li[i] < li[i + 1]:
        a += li[i + 1] - li[i]
    else:
        result.append(a)
        a = 0
result.append(a)
print(max(result))
