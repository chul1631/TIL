# 1. [3, 10, 20] 평균 구하기
numbers = [3, 10, 20]
# 2. 값 초기화
result = 0 
count = 0

# 3. 반복
for number in numbers:
    result = result + number
    count = count +1
print(result/count)