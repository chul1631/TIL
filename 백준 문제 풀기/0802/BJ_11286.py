# 힙은 언제 사용해야 할까?
# 1. 데이터가 지속적으로 정렬되야 하는 경우
# 2. 데이터에 삽입/삭제가 빈번할 때

import sys
import heapq

numbers = int(input())
heap = []

# heap을 tuple로 구성했을 때 맨 앞 숫자만 가지고 정렬하므로 앞은 
# abs함수를 써주고 두 번째는 원래 수를 써줌으로써 절댓값 정렬을 할 수 있게 한다.

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

# 힙(Heap)
# 힙의 특징
# 최대값 또는 최소값을 빠르게 찾아내도록 만들어진 데이터구조
# 완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지한다
# 느슨한 정렬 상태 : 내가 목표하는 바를 이루되 나머지는 그러하지 않은 것
# 즉, 최대/최소 값을 출력하길 원한다 그 값은 무조건 왼쪽 끝에 출력되게끔 정렬되지만
# 나머지도 그렇게 정렬되는 것은 아님
# min을 예로 들면 왼쪽 끝 값이 pop으로 빠져나가면 다시 최소값을 맨 왼쪽에 정렬
# 힙 트리에서는 중복 값을 허용한다


