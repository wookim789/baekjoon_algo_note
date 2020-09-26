n = int(input())
m = int(input())

edge_list = [[] for _ in range(n + 1)]
for i in range(m):
    f_idx, b_idx = map(int, input().split())
    edge_list[f_idx].append(b_idx)
    edge_list[b_idx].append(f_idx)

# dfs, bfs 둘다 가능
# bfs가 평균적으로 성능이 더 좋기에 bfs로 구현

from collections import deque
visited = [False] * (n+1)
def bfs(st_idx, edge_list, visited):
    result = 0
    que = deque()

    que.append(st_idx)
    visited[st_idx] = True
    while que:
        cur_idx = que.popleft()

        for edge in edge_list[cur_idx]:
            if not visited[edge]:
                que.append(edge)
                visited[edge] = True
                result += 1
    print(result)

bfs(1, edge_list, visited)