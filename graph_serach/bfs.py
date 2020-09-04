# BFS 구현
# que를 이용해 구현한다 collections의 deque 라이브러리를 사용한다
# 일반적으로 DFS보다 실행속도가 빠르다

from collections import deque

def bfs(graph, visited, start):
    # 첫 노드를 방문처리
    visited[start] = True

    # 첫 노드 큐에 삽입
    que = deque()
    que.append(start)

    # 첫 노드와 인접한 노드들을 방문처리하고 큐에 삽입
    # 큐가 빌때까지 반복
    while que:
        idx = que.popleft()
        print(idx, end = ' ')
        for v in graph[idx]:
            if not visited[v]:
                # 인접한 노드 방문처리
                visited[v] = True
                que.append(v)
                

graph = [
        [],      # 연결되지 않은 노드
        [2,3,8], # 1과 연결된 노드
        [1,7],   # 2와 연결된 노드
        [1,4,5], # 3 "
        [3,5],   # 4 "
        [3,4],   # 5 "
        [7],     # 6 "
        [2,6,8], # 7 "
        [1,7]    # 8 "
    ]

visit = [False] * 9

bfs(graph, visit, 1)