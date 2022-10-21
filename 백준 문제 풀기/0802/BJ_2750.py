import sys
sys.stdin = open("input2.txt")

n = int(input())
m = []
for i in range (n):
    m.append(input())
o = sorted(m)
print(*o,sep='\n')
