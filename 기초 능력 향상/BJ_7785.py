import sys

sys.stdin = open("BJ_7785.txt")

ent = dict()
for i in range(int(input())):
    a, b = input().rstrip().split()
    if b == "enter":
        ent[a] = True
    else:
        ent.pop(a)
print(*sorted(list(ent.keys()), reverse=True), sep="\n")
