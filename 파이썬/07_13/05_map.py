numbers = ['1', '2', '3']
#숫자로 바꿔서 쓰고 싶을때
#리스트를 숫자로 형 변환은 불가능.
#다만, 숫자 형태의 문자를 변환할 수 는 있음.
# n = int(numbers)

#가능 but 100,1000개 일때는? -> 반복문!
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
print(numbers)

new_numbers =[]
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# map!
numbers = ['1', '2','3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2) # <map object at 0x000002277A735FA0>
print(list(new_numbers)) #<- 리스트로 형 변환 해서 보면 바껴있음.
