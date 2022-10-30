import sys

sys.stdin = open(
    "BJ_2798.txt",
)

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

max_sum = 0
for x in range(N):
    for y in range(x + 1, N):
        for z in range(y + 1, N):
            ch_ = num_list[x] + num_list[y] + num_list[z]
            if (max_sum < ch_) & (M >= ch_):
                max_sum = ch_
print(max_sum)
