import heapq
INF = int(1e9)
distance = []
graph = []
def solution(n, s, a, b, fares):
    global INF, distance, graph
    answer = 0
    

    distance = [INF] * (n + 1)
    print(distance, s)
    graph = [[]for i in range(n + 1)]
    
    for arr in fares:
        graph[arr[0]].append([(arr[1]), arr[2]])
        graph[arr[1]].append([(arr[0]), arr[2]])
    
    # print(graph)
    dijkstra(s)
    
    
    return answer
def dijkstra(s):
    global INF, distance, graph
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, s))
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    distance[s] = 0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 (튜플이다)
        dist, now_node_idx = heapq.heappop(q) 
        print(dist, now_node_idx)
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
    print(distance)

# solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])