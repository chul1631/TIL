# 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점
# 1 번째 줄부터 10 번째 줄에는 W 대학의 각 참가자의 점수를 나타내는 정수가 11 번째 줄부터 20 번째 줄에는 K 대학의 각 참가자의 점수

# W대학
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

# K대학
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



import sys
input = sys.stdin.readline

W = [] 
K = [] 

for i in range(10):
    W.append(int(input()))

for i in range(10):
    K.append(int(input()))

# W,K 내림차순 정렬
W.sort(reverse=True)
K.sort(reverse=True)

W_sum = 0
K_sum = 0

# 득점이 높은 사람에서 3 명의 점수를 합산
for i in range(3):
    W_sum += W[i]
    K_sum += K[i]

# 출력 
print(W_sum,K_sum)
