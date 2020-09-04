# 개선된 다익스트라 알고리즘
# 배열을 선형탐색하지않고 
# 힙 자료구조를 사용한다
# 힙은 heapq 라이브러리를 이용한다

import heapq
import sys


# 입력 순서
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[]for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    distance[start] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (튜플이다)
        dist, now_node_idx = heapq.heappop(q) 

        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now_node_idx] < dist:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node_info in graph[now_node_idx]:
            # node_info = [0, 1] : node_info[0]은 노드 인덱스, node_info[1]은 거리 비용
            # noew_node_idx와 연결된 다른 노드의 정보를 가져온거다 
            idx = node_info[0]
            node_dist = node_info[1]
            cost = dist + node_dist

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < distance[idx]:
                distance[idx] = cost
                heapq.heappush(q, (cost, idx))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    #  도달할 수 없는 경우, 무한으로 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])