graph =[]
visited = [False] * n # 방문 처리 리스트 만들기

def dfs(start):
    stack = [start] # 돌아갈 곳을 기록
    visited[start] = True # 시작 정점 방문 처리

    while stack : #스택이 빌때 까지 반복
        cur = stack.pop() #현재 방문 정점(후입선출)

        for adj graph[cur]: # 인접한 모든 정점 방문하지 않았다면

            if not visited[adj]: 
                visited[adj] = True #방문처리
                stack.append(adj) #스택에ㅔ 넣