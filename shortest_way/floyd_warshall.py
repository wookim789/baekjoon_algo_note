# 시작지점이 정해져 있지 않고
# 모든 노드와 모든 노드간의 최단 경로를 2차원 배열에 전부 기록
# dp 알고리즘


INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2 차원 리스트(그래프 표현)를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

# for i in range(n+1):
#     graph[i][i] = 0

# 위 for문과 동일한 로직
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

# 2차원 리스트 확인
# for i in graph:
#     print(i)



# 입력 예
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    
# 수행된 결과를 출력
for a in range(0, n + 1):
    for b in range(0, n + 1):
        # 도달할 수 없는 경우 무한으로 출력
        if graph[a][b] == INF:
            print("INFINITY", end =' ')
        else:
            print(graph[a][b], end= ' ')
    print()

# 출력 예
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0
