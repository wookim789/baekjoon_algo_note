# 도시 분할 계획
# 2
# 40
# 2 128

# 최소 신장트리를 구하고나서 가장 비용이 큰 간선을 제거한다
# 마을 -> 최소신장 트리 구하기
# 마을A 마을B로 나누기 
# 최소신장은 어떻게 구한다?
# 마을이 하나일 떄 최소 신장 트리 구한다음에 (크루스칼 알고리즘)
# 가장 마지막의 비용이 큰 간선 하나를 뚝 짜르면
# 만족한다
def find_parent(parent, x):
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

# v, e = map(int, input().split())
v, e= 7, 12

parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모테이블 -> 자기 자신을 부모로 초기화
for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

# # 모든 간선 정보 입력 받기
# for i in range(e):
#     a, b, cost = map(int, input().split())
#     # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
#     edges.append((cost, a, b))

edges.append((3, 1, 2))
edges.append((2, 1, 3))
edges.append((1, 3, 2))
edges.append((2, 2, 5))
edges.append((4, 3, 4))
edges.append((6, 7, 3))
edges.append((5, 5, 1))
edges.append((2, 1, 6))
edges.append((1, 6, 4))
edges.append((3, 6, 5))
edges.append((3, 4, 5))
edges.append((4, 6, 7))

# 간선을 비용순으로 정렬
edges.sort()
last = 0
# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    
    # 사이클이 방생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        # 트리로 추가 할때만 last 갱신
        # 반복되면서 가장 마지막의 최대 비용으로 last가 변경됨
        last = cost
print(parent)
print(result - last)


