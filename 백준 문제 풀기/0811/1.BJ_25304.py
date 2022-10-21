import sys

sys.stdin = open("BJ_25304.txt","r")

# 첫째 줄 영수증에 적힌 총 금액 X
X = int(input())
# 둘째 줄 영수증에 적힌 구맿나 물건의 종류의 수 N
N = int(input())

# 총 액수
sum = 0 

# N개의 줄에는 각 물건의 가격 a와 개수b, 공백을 사이에 두고 주어진다.
for i in range (N): 
    a,b = map(int,input().split())
# 총 액수 = 물건의 가격 x 개수
    sum += a*b

# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사.
if  sum == X: print("Yes")
else: print("No")
