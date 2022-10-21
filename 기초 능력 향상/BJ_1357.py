import sys
sys.stdin = open("BJ_1357.txt")

x, y = map(str, input().split())
s = str(int(x[::-1]) + int(y[::-1]))
print(int(s[::-1]))