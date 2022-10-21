import sys
sys.stdin = open("SWEA_2050.txt")

k = list(input())
for i in range(len(k)):
    print(ord(k[i])-64, end=' ')