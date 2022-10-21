import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for i in range(1, T+1):
    case = int(input())
    grade = list(map(int, input().split()))
    arr = [0] * 101
    for i in grade:
        arr[i] += 1
    target = max(arr)
    print("#{} {}".format(i, arr.index(target)))
