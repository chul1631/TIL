import sys
sys.stdin = open("BJ_11720.txt")

n = input()
nums = input()
total = 0
for i in nums :
    total += int(i) 
print(total)