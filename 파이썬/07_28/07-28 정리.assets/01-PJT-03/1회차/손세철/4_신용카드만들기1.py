import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

# 테스트 케이스 수 T만큼 반복
for testcase in range(T):

# 카드 15자리 숫자 입력
    card = input().split()
# 변수 선언

    card_sum = 0
# card 15자리 숫자 하나씩 반복
for i in range(0, len(card)):
# 매 홀수자리 숫자 2배로 만들고 더해줌
    if (i+1) % 2 != 0:
        card_sum += int(card[i]) * 2
# 짝수의 경우 그냥 더해줌
    else:

        card_sum += int (card[0]) + int (card[1])   

if  card_sum > 9:
    numbers = str(card)
# 10으로 나누어 지면 0... 
if (card_sum //10) : 0

#출력..
print(f"#{i} {card_sum}")
