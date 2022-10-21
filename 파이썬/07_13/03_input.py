print('hi', 'hello', sep='-')


def my_add(*numbers):
    return numbers

my_add(1, 2, 3)
result = my_add(1, 2, 3)
print(result, type(result))


def my_func(**kwargs):
    return kwargs
result = my_func(name='손세철', age='30ㅠㅠ', gander='M' )

print(result, type(result))