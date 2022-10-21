import sys

sys.stdin = open("BJ_2979.txt","r")
# 주차 요금 구하는 문제

# 첫째 줄에 문제에서 설명한 주차 요금 A, B, C가 주어진다.

# 다음 세 개 줄에는 두 정수가 주어진다. 

# 이 정수는 상근이가 가지고 있는 트럭이 주차장에 도착한 시간과 주차장에서 떠난 시간이다. 도착한 시간은 항상 떠난 시간보다 앞선다.

# A B C
# 5 3 1

# 도착시간  떠난시간
#   1         6
#   3         5
#   2         8

A,B,C = map(int,input().split())
truck1 = list(map(int,input().split()))
truck2 = list(map(int,input().split()))
truck3 = list(map(int,input().split()))

# 떠난 시간을 저장하는 변수 선언
Last = max(truck1[1],truck2[1],truck3[1])

# 주차요금 저장할 변수 선언
Fee = 0

# 세 트럭 중 가장 마지막에 떠나는 시간까지 1부터 반복
for i in range(1, Last+1):

# 주차장에 있는 트럭 개수 저장할 변수 선언
    count = 0
    
# 현재 첫번째 트럭이 있다면 트럭 개수에 +1
    if truck1[0] < i <= truck1[1]:
        count += 1
    if truck2[0] < i <= truck2[1]:
        count += 1
    if truck3[0] < i <= truck3[1]:
        count += 1       

# 주차장에 트럭 1대라면
if count == 1:
# A요금 * 트럭 대수
    Fee += A * count
# 2대
elif count == 2:
    Fee += B * count
# 3대
elif count == 3:
    Fee += C * count

print(Fee)