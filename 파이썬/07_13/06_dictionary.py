# 기본 순회
# key가 기준이고, 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다.

my_dict = {'apple': '사과', 'banana': '바나나'}
print(my_dict['apple']) #사과

for word in my_dict:
    print(word, my_dict[word]) # 'apple', 'banana'

# 다양한 방법
print(my_dict.keys())
# => 일종의 리스트라고 생각해서 사용하면 됨
for value in my_dict.values():
    print(value)
print(my_dict.values())
print(my_dict.items())
for k, v in my_dict.items():
# k,v = 함수나 동작을 하는게 아님 => just 이름 붙이는 영역이라고 생각 하면됨
    print(k,v)
# 일종의 리스트안에, tuple
# dict_items([('apple', '사과'), ('banana', '바나나')])


my_dict_2 = {}
my_dict_2['a'] = 'airplane'

my_dict_3 = {'a': 0}
# my_dict_3 ['a'] +=1
my_dict_3['a'] = my_dict_3['a'] + 1
print(my_dict_3)

my_list = [10, 11, 12]
my_list[0] = my_list[0] + 1

for word in my_dict:
    print(my_dict[word])