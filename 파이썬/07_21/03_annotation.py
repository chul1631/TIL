# 변수 어노테이션
a: int = 3
print(a)

# 함수 어노테이션
def add(x:int, y:int) ->int:
    return x + y

print(add(7,4))
print(add('hi', 'hello'))

# 함수 어노테이션

def add2(x,y):
    return x + y    
print(add2(7,4))
