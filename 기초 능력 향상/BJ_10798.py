import sys

sys.stdin = open("BJ_10798.txt")

words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end="")
