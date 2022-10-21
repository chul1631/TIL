# 인풋값 
N = int(input())

# 인풋값과 비교하기 위한 변수
result = 0 

#for문 1~N까지 순회
for i in  range(1, N+1):
# str함수를 통해 i의 각 자리수를 A리스트에 넣기
    A = list(map(int,str(i)))
 # 분해합 256(245+2+4+5) 그대로인 값 i와 각 자리수가 들어간 A리스트의 합를 더함
    result = i + sum(A)
    if result == N:
        print(i)
        break
# 생성자 없을 경우 0 출력
    if i ==N:
        print(0)