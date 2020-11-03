# 서로소 집합 알고리즘


# 특정 원소가 속한 잡힙을 찾기

# 입력 예시
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

######################################## 중요 ##################################################

def find_parent(parent, x):
    # 자신의 노드와 부모 노드가 같지 않다 = 자식 노드(루트가 아니다)
    if parent[x] != x:
        # # 재귀 호출
        # return find_parent(parent, parent[x])
        # 찾을떄 까지 반복되는 재귀 호출은 성능 문제가 있으므로 
        # 경로압축 기법을 이용한다
        # 자신의 루트를 찾기위해 부모를 타고 타고 오르지 않는다.
        # 같은 집합일 경우 모두 부모가 루트로 설정되도록 경로를 압축(갱신)한다
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

######################################## 중요 ##################################################


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

# union 연산
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 
print('원소 집합 :', end ='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 출력

print('부모 테이블:', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')


# 원소 집합 :1 1 1 1 5 5
# 부모 테이블:1 1 2 1 5 5