# . = 빈자리
# X = 짐이있음

# 행과 열 각각 탐색, 카운트 
# .이 2개이상이면 누울수 있음,cnt 증가,  X만날 시 cnt 초기화
# 줄이 바뀔때 cnt 0으로초기화


N = int(input())
matrix = [list(map(str, input())) for _ in range(N)]

# matrix = [
# ....X
# ..XX.
# .....
# .XX..
# X....
#]


# matrix list 
# [0,1,2,3,4 = [....X] ]
# [0,1,2,3,4 = [..XX.] ]
# [0,1,2,3,4 = [.....] ]
# [0,1,2,3,4 = [.XX..] ]
# [0,1,2,3,4 = [X....] ]

# 행,열 값 초기화
row = 0
col = 0

# 행
for j in range(N): #0~4까지 순회
    cnt = 0 # cnt 값 초기화
    for i in range(N): # 0~4까지 순회
        if matrix[j][i] == '.':
            cnt += 1
        elif matrix[j][i] == 'X':
            if cnt >= 2:
                row += 1
            cnt = 0
            if cnt >= 2:
                row += 1
            cnt = 0

# [0,1,2,3,4 => ....+1X] = 0~4 순회하면서 .연속해서 2개 이상인 경우 cnt +=1 씩,
# [0,1,2,3,4 => ..XX.]   만약 2이상인 경우 cnt 값 초기화 시켜줌.
# [0,1,2,3,4 => .....]
# [0,1,2,3,4 => .XX..]
# [0,1,2,3,4 => X....]



#열
for i in range(N):
    cnt = 0
    for j in range(N):
        if matrix[j][i] == '.':
            cnt += 1
        elif matrix[j][i] == 'X':
            if cnt >= 2:
                col += 1
            cnt = 0
    if cnt >= 2:
        col += 1
    cnt = 0


print(row, col)


