# 파일명, 어떤모드로 열지,
# 인코딩을 설정
with open('students.txt', 'r', encoding= 'utf-8') as f:
    # 텍스트는 string 타입
    text = f.read()
    print(test, type(text))
    # string.split() =>list 타입
    names = text.split()
    cnt = 0
    for name in names:
        # name : 첫번째 시행 - 이름
        # 언제? 김씨?
        if name.startswith('김'):
        # if name[0] == '김':
            cnt += 1
        print(cnt)