# x라는 리스트 만들어줌
x = []
# input값 만들어준 리스트에 반복해서 추가
for i in range(5):
    x.append(int(input()))
# 평균값 sum사용 input값 다 더해준 뒤 input값 만큼 나눠준다.
print(int(sum(x)/ 5))

# 중간값을 구해야 하니 오름차순 정렬 후 중간에있는 값 출력
x.sort()
print(x[2])