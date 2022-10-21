import sys
sys.stdin = open("최소,최대.txt")

N = input()
num_list = list(map(int,input().split()))
print(min(num_list), max(num_list))