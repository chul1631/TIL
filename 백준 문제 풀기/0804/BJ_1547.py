cup = [0, 1, 0, 0]
for _ in range(int(input())):
    x, y = map(int, input().split())
cup[x], cup[y] = cup[y], cup[x]
print(cup.index(1))