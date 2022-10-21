#  리스트에 개수 저장
list_ = [1, 1, 2, 2, 2, 8]
# data 리스트에 input값 받음
data = list(map(int, input().split()))
# for 반복문 통해  리스트 i 번쨰 인덱스 값에서 data 리스트 i 번째 인덱스 값을 빼고 출력.
for i in range(6) :
  print(list[i] - data[i], end=' ')