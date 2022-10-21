import sys

text = sys.stdin.read()
text = text.replace('\n', '').replace(' ', '')

alpha = [0 for i in range(26)]

for i in range(len(text)):
  word = ord(text[i]) - 97
  alpha[word] += 1

for i in range(26):
  if alpha[i] == max(alpha):
    print(chr(97+i), end='')