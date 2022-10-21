# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.

import sys

sys.stdin = open("BJ_2857.txt","r")

# "FBI"가 있다면 추가해줄 빈 리스트 작성
agent = []

# for문 사용 1~5까지 넣어줌.
for i in range(1,6):
    a = input()
# 만약 FBI 단어가 인풋값에 들어있으면 agent리스트에 추가    
    if "FBI" in a:
        agent.append(i)

# 그냥 출력하면 리스트 형태로 나오니 asterisk(*) 사용하여 unpacking해준다.
if agent:
    print(*agent)
else:
    print("HE GOT AWAY!")
