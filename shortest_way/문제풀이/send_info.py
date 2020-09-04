# 전보
# 3
# 60분
# 1초, 128mb
# 7시 20분 까지


# N개의 도시
# x -> y 있음
# x <- y 없음
# 위 경우 y는 x에 전보 못 보냄

# c도시와 연결 가능한 도시의 수
# 도시들이 모두 메시지를 받는 데까지 걸린 시간의 합

# 시작 도시는 고정
# 다익스트라의 결과물
# 시작 지점으로부터 각 노드의 최소 이동 비용

# 다익스트라 문제

import heapq

INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[]for i in range(n+1)]

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

print()
count = 0
mount = 0
for i in distance:
    if i != INF and i != 0:
        count += 1
        mount = max(mount, i)
print(count, mount)