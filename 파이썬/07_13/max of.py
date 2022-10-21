numbers = [0, 20, 100]

#초기화
if int(numbers[0]) > int(numbers[1]):
    max = int(numbers[0])
    second = int(numbers[1])
else:
    max = int(numbers[1])
    second = int(numbers[0])

for i in numbers:
    if(int(i) > max):
        second = max
        max = int(i)
    elif(int(i) > second):
        if int(i) == max: #중복되는 수 제거
            continue
        second = int(i) 
print(second)