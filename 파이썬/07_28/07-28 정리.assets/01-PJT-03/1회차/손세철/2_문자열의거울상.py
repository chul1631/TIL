import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for i in range(1, 1+T):
    arr = list(input())
    # 딕셔너리 활용 
    mirror = {'b' : 'd', 'd':'b', 'q':'p', 'p':'q'}
    result = ''
    arr.reverse
    for i in arr:
        result += mirror[i]
print(f"#{i} {result}")
