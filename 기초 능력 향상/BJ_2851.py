import sys

sys.stdin = open("BJ_2851.txt")

scores = 0
for _ in range(10):
    score = int(sys.stdin.readline())
    pre_scores = scores
    scores += score
    if scores >= 100:
        if abs(100 - scores) > abs(100 - pre_scores):
            scores = pre_scores
        break
print(scores)
