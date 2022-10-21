import sys
input = sys.stdin.readline
# W , K대학 
W = [] 
K = [] 

# W 대학 입력
for i in range(10):
    W.append(int(input()))


# K 대학 입력
for i in range(10):
    K.append(int(input()))

# W,K 내림차순 정렬
W.sort(reverse=True)
K.sort(reverse=True)

Wsum = 0
Ksum = 0

# 3등까지의 합 구하기
for i in range(3):
    Wsum += W[i]
    Ksum += K[i]

# 출력 
print(Wsum,Ksum)

# 23
# 23
# 20
# 15
# 15
# 14
# 13
# 9
# 7
# 6
# 25
# 19
# 17
# 17
# 16
# 13
# 12
# 11
# 9
# 5