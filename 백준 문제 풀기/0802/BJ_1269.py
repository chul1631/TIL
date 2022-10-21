# SET 언제 사용?
# 1. 데이터의 중복이 없어야할때
# 2. 정수가 아닌 데이터의 삽입/ 삭제/ 탐색이 빈번히 필요할 때

# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).

# Set의 연산자
# .add()
# .remove()
# +  합
# -  차
# &  교
# ^  대칭차
# 대칭 차집합?
#   두집합 A,B 둘중 하나에 포함되지만 두 집합 모두에 포함되지 않는 원소들의 모임
import sys
sys.stdin = open("input.txt")

n,m = map(int, input().split())
a = set(map(int,input().split())) # 1 2 4
b = set(map(int,input().split())) # 2 3 4 5 6
print(len(a^b)) # 1 3 5 6 len=>4

