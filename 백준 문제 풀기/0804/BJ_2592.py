N = []
for i in range(10):
    N.append(int(input()))
print(sum(N)//10)

num = 0 # 최빈값 개수
print(max(N, key = N.count))
