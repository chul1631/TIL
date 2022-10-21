#예제 07. [오류 해결] 평균 구하기

# count 들여쓰기 오류

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
count = 0
for number in number_list:
    total += number
    count += 1
print(total // count)