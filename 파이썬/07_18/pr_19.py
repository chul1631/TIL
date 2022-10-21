# 문제 19. 숫자의 길이 구하기

number = 123

# 1. 문자열로 형변환
print(len(str(number)))


# 2. while
number = 123
cnt = 0
while number != 0:
    number //= number // 10
    cnt +1
print(cnt)

# 3.log
import math
number = 123456
print(int(math.log(number, 10)) +1)