import sys

sys.stdin = open("BJ_2747.txt", "r")

n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
print(a)
