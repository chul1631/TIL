# 예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기

#  AttributeError: 'tuple' object has no attribute 'append'
# 튜플은 append 메소드를 사용하여 새로운 요소 추가 불가능 (수정 할 수 없음)

N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)