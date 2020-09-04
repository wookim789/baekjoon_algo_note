# 커리큘럼
# 3
# 50분
# 2 128mb

# 선수 강의 -> 위상정렬 문제
# 특이하게 위상정렬에 코스트가 있다

from collections import deque
import copy

v = int(input())

# cost <= 100,000
indegree = [0] * (v + 1)
time = [0] * (v+1)

graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력하기
for i in range(1, v +1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 시간
    for x in data[1:-1]: # 2번째 수부터 맨마지막 전까지   ex 0 1 2 3  -> 1, 2
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v + 1):
        print(result[i])
topology_sort()