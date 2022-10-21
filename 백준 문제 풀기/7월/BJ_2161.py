import sys
sys.stdin = open("input.txt")
n = int(input()) 

card = [] 
card2 = [] 

for i in range(1, n+1): 
    card.append(i) # card 리스트에 input값 추가


while True: 
    card2.append(card.pop(0)) # card 리스트에 제일 위에 있는 카드를 버린다. 
                                # pop() 리스트 맨 마지막 요소 돌려주고 그 요소 삭제
    if not card:
        break  # 위에서 card 를 팝 했을 때 남은 card 가 없으면 멈춘다.
    card.append(card.pop(0)) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.


print(card2)

#---------------------------------------------------------------------------------------------
#deque
# from collections import deque

# n = int(input())
# queue = deque(range(1,1+n))

# while len(queue) > 1:
#     print(queue.popleft(), end=" ")
#     queue.append(queue.popleft())
# print(queue[0])
# #-------------------------------------------------
# # queue
# n = int(input())
# queue = list(range(1,n+1))
# while len(queue) >1:
#     print(queue.pop(0), end = " ")
#     queue.append(queue.pop(0))
# print(queue[0])