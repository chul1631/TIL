import sys
sys.stdin = open("두 수 비교하기.txt")

A,B = map(int,input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')