T = int(input())
for i in range(1, T+1):
    a = input()
    if a == a[::-1]:
        print("#%d" %i, 1)
    else:
        print("#%d" %i, 0)