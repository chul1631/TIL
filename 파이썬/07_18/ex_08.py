# 예제 08. [오류 해결] 모음의 개수 찾기
word = "HappyHacking"

count = 0

for char in word:
    if char in  ["a" or "e" or "i" or "o" or "u"]:
        count += 1

print(count)
