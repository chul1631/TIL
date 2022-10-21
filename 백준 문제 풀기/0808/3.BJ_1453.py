# 거절 당하는 사람의 수.

n = int(input())  # input

x = list(map(int, input().split()))  # 손님이 앉고 싶어하는 자리

cnt = 0  # 거절당하는 사람의 수

seat = []  # 피시방 자리
for i in range(n):
    if x[i] in seat: # 앉고 싶어하는 자리에 사람이 있으면
        cnt += 1   # 거절당하는 사람의수에 더함
    else: # 자리에 사람이 없다면
        seat.append(x[i]) # 더해줌
print(cnt)
