# 스택과 동일한 형태의 탐색 알고리즘
# 재귀함수 구조로 작성 시 간단하게 작성 가능
# 연결된 노드들을 탐색 할때, 가장 깊게 연결된 것부터 탐색하는 알고리즘


def dfs(graph, visit, idx):
    visit[idx] = True
    print(idx, end =' ')
    for v in graph[idx]:
        if not visit[v]:
            dfs(graph, visit, v)


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

# 그래프가 위와 같을 때, dfs 탐색알고리즘으로 탐색순서를 출력하라
visit = [False for _ in range(9)] 
print(visit)

dfs(graph, visit, 1)