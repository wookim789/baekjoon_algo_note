# 미래도시
# 2
# 40분
# 1초 128mb
# 6시 10분까지

# 현재 위치 고정 -> 다익스트라? 
# 1번 위치에서 x 회사 방문하여 판매
# 모든 도로간 비용은 1
# 소개팅상대난 k 회사

# 1 -> k -> x 
# 위 경로를 지날 수 있는 최단 시간 구하기
# 최소비용구하기
# => 요구 조건이 모든 경로를 지나는 최단경로를 구하는 것이기 
# 플로이드 워셜 문제다

INF = int(1e9)

# 둘다 100 이하
n, m = map(int, (input().split()))

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, (input().split()))

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    
# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우 무한으로 출력
        if graph[a][b] == INF:
            print("I", end =' ')
        else:
            print(graph[a][b], end= ' ')
    print()

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)