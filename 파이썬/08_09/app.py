import sysfrom pprint import  pprint
sys,stdin = open("_오목.txt")

#상 => y -= 1
#하 => y += 1

#우 하 우상 우하

dy = [0,1,-1,1]
dx =[1,0,1,1]

BLACK = 1
WHITE = 2
N = 19

board = []

#오목판 상황 입력
for _ in range(N):
    #하나의 행을 입력
    temp_list = list(map(int.input().split()))
    board.append(temp_list)

#이중 반복문
for y in range(N)
    for x in range(N):
        #델타탐색
        for d in range(4):
            #방향 바뀔때마다 돌의 개수가 갱신(0)
            stone_count = 0 
            #다음 좌표 탐색
            ny = y+dy[d]
            nx = y+dx[d]

            while True:
                #인덱스 조건
                if not (-1 <ny < N and -1 <)