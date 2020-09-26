# dfs #bfs

n, m, st_idx = map(int, input().split())

edge_list = [[] for _ in range(n+1)]

for i in range(m):
    f_idx, b_val = map(int, input().split())
    edge_list[f_idx].append(b_val)
    edge_list[b_val].append(f_idx)

for edge in edge_list:
    edge.sort()

visited = [False] * (n+1)
# dfs는 재귀적으로 구현한다
def dfs(st_idx, edge_list, visited):
    if visited[st_idx] == True:
        return
    
    # 방문 처리
    visited[st_idx] = True
    print(st_idx, end =' ')

    for edge in edge_list[st_idx]:
        dfs(edge, edge_list, visited)
    return

dfs(st_idx, edge_list, visited)
print()

# bfs 구현
# bfs는 큐을 사용한다

from collections import deque
visited = [False] * (n + 1)
def bfs(st_idx, edge_list):
    que = deque()

    que.append(st_idx)
    visited[st_idx] = True
    print(st_idx, end =' ')
    # 큐가 빌떄 까지
    while que:
        cur_idx = que.popleft()
        for edge in edge_list[cur_idx]:
            if not visited[edge]:
                que.append(edge)
                visited[edge] = True
                print(edge, end =' ')


bfs(st_idx, edge_list)