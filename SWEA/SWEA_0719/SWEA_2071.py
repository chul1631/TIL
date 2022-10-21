T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    answer = 0
    for nums in numbers:
        answer += nums
    answer /= 10
    print("#{} {}".format(i+1, round(answer)))

