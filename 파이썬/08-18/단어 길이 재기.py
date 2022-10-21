import sys
sys.stdin = open("단어 길이 재기.txt")

word = input()
word_lst = list(word)
print(len(word_lst))