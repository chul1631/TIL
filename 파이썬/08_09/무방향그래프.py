
graph = []

N = 7 # 정점 개수
M = 7 # 간선 개수

# N x N 행렬 초기화
# 0이 초기화 되어있는 N을 N만큼 반복
matrix = [[0]*N for i in range(N)]


for i in range(M):
    # v1, v2 = map(int, input().split())
    v1, v2 = edge = [0], edge [1]

    graph[v1][v2] = 1
    graph[v2][v1] = 1
    

print(graph)

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6