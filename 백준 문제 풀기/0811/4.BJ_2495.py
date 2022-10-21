# 여덟 자리의 양의 정수가 주어질 때, 
# 1) 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력, 
# 2) 있다면 연속된 숫자의 길이 가장 긴 것 출력

import sys

sys.stdin = open("BJ_2495.txt","r")

# 각 줄에 하나씩 세 개의 양의 정수 주어짐
for _ in range(3): 
# 리스트로 input값 받아줌  
  num = list(input()) 
# 첫번째 숫자 담기 
  arr = [num[0]]
# 연속하여 같은 숫자가 나오는 것이 없으면 1을 출력하기 위해 1을 저장해둠
  answer = [1] 
# arr에 숫자가 하나 담겼기 때문에 cnt에 1 저장
  cnt = 1 
# 숫자는 여덟 자리이기 때문에 7번 반복
  for i in range(1, 8):
# arr에 담겨있는 숫자와 현재 숫자가 같다면 1을 더해준다.
    if(arr[len(arr)-1]==num[i]):
      cnt += 1
# 다르면 그 수를 arr에 추가하고 cnt값을 answer에 저장, cnt는 1로 초기화
    else:
      arr.append(num[i])
      answer.append(cnt)
      cnt = 1 
 # 계속해서 arr에 담겨있는 숫자와 현재 숫자가 같아 저장이 되지 않았을 cnt를 위해서 answer에 cnt추가
  answer.append(cnt)

# 가장 큰 값을 출력하기 위해서 max 사용
  print(max(answer))