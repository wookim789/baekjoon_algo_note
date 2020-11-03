# 크루스칼 알고리즘 
# 그래프의 최소 신장 트리 연결 비용을 구할때 사용한다

# 최소 신장 트리 : 노드간 연결이 cycle 없이 구성될 때, 비용이 가장 적게 간선을 연결한 트리

# 그리드 알고리즘에 포함되고

# 간선의 개수가 e개일 때 O(ElogE)의 시간 복잡도를 가진다
# 간선 정렬에 시간이 오래걸리는 알고리즘

# 이거이거 정렬하는 알고리즘을 사용안할려면
# 그래프를 우선순위큐에 비용및 연결정보를 저장해서 꺼내다 쓰면 되는거자나? -> 계속 열어봐야하는데 우선순위로 쓰면 pop되서 안됨
# 일단 구현먼저 해보고 성능 향상 시켜보자


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 해당 함수를 2가지로 구현할 수 있다

    # 만약 연결 정보가 필요하다면 1번  
    # if parent[x] != x:
    #     return find_parent(parent, parent[x])

    # 경로압축 최소 비용만을 얻어야 한다면 2번
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]



# 두원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

# 노드 개수와 간선(union 연산)의 개수 입력 받기
# v, e = map(int, input().split())
v, e = 7, 9

parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모테이블 -> 자기 자신을 부모로 초기화
for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

# 모든 간선 정보 입력 받기
# for i in range(e):
#     a, b, cost = map(int, input().split())
#     # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
#     edges.append((cost, a, b))

edges.append((29, 1, 2))
edges.append((75, 1, 5))
edges.append((35, 2, 3))
edges.append((34, 2, 6))
edges.append((7, 3, 4))
edges.append((23, 4, 6))
edges.append((13, 4, 7))
edges.append((53, 5, 6))
edges.append((25, 6, 7))



# 간선을 비용순으로 정렬
edges.sort()
# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    
    # 사이클이 방생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
    
print(result)


# 입력 예
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
# 최소 비용
# 159