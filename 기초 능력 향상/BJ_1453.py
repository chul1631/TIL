import sys

sys.stdin = open("BJ_1453.txt")

N = int(input())
seats = list(map(int, input().split()))
s = len(list(set(seats)))
print(N - s)
