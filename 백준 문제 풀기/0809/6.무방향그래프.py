edges = []
# 정점 갯수, 간선 갯수
n, m = map(int, input().split())


# 행렬 초기화
graph = [[0] * (n + 1) for _ in range(n + 1)]
# 리스트 초기화
graph2 = [[] for _ in range(n + 1)]

for j in range(m):
    v1, v2 = map(int,input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    graph2[v1].append(v2)
    graph2[v2].append(v1) # 유방향일 때는 이 행 삭제

print(graph)
print(graph2)
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6