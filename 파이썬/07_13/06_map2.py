# 직사각형 넓이 구하시오
# 직사각형 세로n 가로 m
# Input 예시
# 10 20

n,m = map(int, input().split())
print(n*m)

#내장함수 10을 다 더해주는 함수
def plus10(n):
    return n +10

numbers = [10, 20, 30]
new_numbers = list(map(plus10, numbers))
print(new_numbers)