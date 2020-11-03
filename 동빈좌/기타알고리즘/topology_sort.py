# 위상정렬
# 순서가 정해져 있는 일련의 작업을 차례대로 수행할 떄 사용가능
# 알고리즘을 배울려면 자료구조를 알아야해!
# 고금 알고리즘을 배울려면 자료구조, 알고리즘을 알아야 해!

# 자료구조 -> 알고리즘 -> 고급 알고리즘
# 등의 예시가 있겠다.

# 구하려는건 위 자료구조 -> 알고리즘 -> 고급알고리즘 의 작업순서이다

# 위와 같이 순서가 있는 그래프가 주어졌다면
# 알맞은 순서로 노드를 반환하면 된다
# 자세한 내용은 패드에 기록해두었다


from collections import deque

# v, e = map(int, input().split())
v, e = 7, 8

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

print(graph)

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a -> b
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort(indegree):
    result = [] # 수행 결과를 담을 리스트

    q = deque()

    # 처음 시작할때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        result.append(node)

        for edge in graph[node]:
            indegree[edge] -= 1
            if indegree[edge] == 0:
                q.append(edge)
    return result

print(topology_sort(indegree))

# 입력 예
# 1 224
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

# [1, 2, 5, 3, 6, 4, 7]