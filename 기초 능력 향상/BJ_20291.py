import sys

sys.stdin = open("BJ_20291.txt")

n = int(input())

ans = {}

for i in range(n):
    file = input().split(".")[1]
    if file not in ans:
        ans[file] = 1
    else:
        ans[file] += 1

    res = list(ans.keys())
    res.sort()

for k in res:
    print(k, ans[k])
