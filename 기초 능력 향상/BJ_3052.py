import sys

sys.stdin = open("BJ_3052.txt")

arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
print(len(set(arr)))
