# 그래프가 사이클인지 확인

# 입력 예
# 3 3
# 1 2
# 1 3
# 2 3

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합집합 : 루트 재 설정
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 입력한 a, b의 각각의 부모 루트를 비교
    # 더 작은 루트로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())

parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모테이블 -> 자기 자신을 부모로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 사이클 발생 여부
cycle = False

# union 연산
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent,a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('cycle')
else: 
    print('non cycle')