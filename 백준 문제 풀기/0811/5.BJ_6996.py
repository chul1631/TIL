import sys

sys.stdin = open("BJ_6996.txt","r")

T = int(input())

for i in range(T):
    a,b=input().split()
# list화 시켜준 후 정렬
    listA = list(a)
    listB = list(b)
    if sorted(listA) == sorted(listB):
# 정렬한 리스트가 동일하면 "are anagrams.", "아니라면 are NOT anagrams.출력"
        print(a,"&",b,"are anagrams.")
    else:
        print(a,"&",b,"are NOT anagrams.")