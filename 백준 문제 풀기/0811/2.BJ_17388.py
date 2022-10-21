# 일처리가 잘되고 있다면 (세학교 참여도 합이 100 이상) "OK"출력
# 잘안되고 있어 무언의 압박이 필요한 대학 동아리(참여도 가장 낮은 대학) 영문이름 첫단어 출력

import sys

sys.stdin = open("BJ_17388.txt","r")


# 첫 번째 줄에 숭실대학교의 참여도, 고려대학교의 참여도, 한양대학교의 참여도를 의미하는 세 자연수 S, K, H가 공백으로 구분되어 주어진다.
S,K,H = map(int,input().split())

# 세 학교의 참여도의 합 100이상이면 OK출력
if 100 <= S+K+H:
    print("OK")

# 그 외

else :
# 참여도 최솟값 숭실대일때  
    if S == min(S,K,H) :
        print("Soongsil")
# 최솟값 고려대
    elif K == min(S,K,H) :
        print("Korea")
# 최솟값 한양대
    elif H == min(S,K,H) :
        print("Hanyang")
        
