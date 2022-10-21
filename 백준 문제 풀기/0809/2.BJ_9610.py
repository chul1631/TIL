# 각 사분면과 축에 점이 몇개 있는지 구하는 문제.

# input값 정수형으로 변환.
N = int(input())

# 각 사분면과 축에 있는 점의 개수를 저장할 리스트 변수 선언

# Quadrant인덱스 0~3에는 각 사분면에 있는 점의 개수 저장
Quadrant = [0,0,0,0]

# axis_ 인덱스 0에는 축에있는 점의 개수
axis_ = [0]

for point in range(N):
    # 점의 좌표 xi,yi를 공백으로 구분해서 입력, 정수형으로 변환
    xi,yi = map(int, input().split())

    # xi,yi 0보다 큰경우
    if xi > 0 and yi >0:
        # 1사분면 점의 개수 Quadrant[0] +1
        Quadrant[0] += 1
    # xi 0보다 작고, yi 0보다 큰 경우
    elif xi < 0 and yi > 0:
        # 2사분면 점의 개수 Quadrant[1] +1
        Quadrant[1] += 1
    # xi,yi가 0보다 작은 경우
    elif xi <0 and yi <0:
        # 3사분면 점의 개수 Quadrant[2] +1
        Quadrant[2] +=1
    # xi가 0보다 크고, yi는 0보다 작은경우
    elif xi > 0 and yi < 0 :
    # 4사분면 점의 개수 Quadrant[3] +1
        Quadrant[3] += 1
   
   # xi, yi중 둘 중 하나가 0이라면
    elif xi == 0 or yi == 0:
        #축의 점의 개수인  axis_[0]에 1을 더해준다.
        axis_[0] += 1

#출력
print(f'Q1: {Quadrant[0]}')
print(f'Q2: {Quadrant[1]}')
print(f'Q3: {Quadrant[2]}')
print(f'Q4: {Quadrant[3]}')
print(f'AXIS: {axis_[0]}')
