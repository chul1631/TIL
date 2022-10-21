# 모음을 리스트형으로 만들어 놓음
vowel = ['a','e','i','o','u']


while True:
    cnt = 0
    # 문자열을 리스트로 입력받되, 소문자로 변경
    s = list(input().lower())
    # 만약 '#'을 첫 글자로 입력받으면 종료
    if s[0] == '#':
        break
    # s의 문자열에 aeiou에 해당하는 문자열이 있을 경우 cnt 1씩 추가
    for i in s:
        if i in vowel:
            cnt += 1
    print(cnt)