# 2차원 행렬(인접리스트) DFS 

# 0 과 1로 구분된 행렬
# 0으로 구성된 영역의 수 찾기

# n, m = map(int, input().split())
# matrix = [[0] * m for _ in range(n)]
# print(matrix)

# 완전 탐색 문제 
# 2차원 행렬을 탐색해야 함 -> dfs or bfs
# dfs로 풀어보자

n, m = 4, 5
matrix = [[0, 0, 1, 1, 0]
        , [0, 0, 0, 1, 1]
        , [1, 1, 1, 1, 1]
        , [0, 0, 0, 0, 0]]

# d l u r
direc = [0, 1, 2, 3]
dx = [0, -1, 0, 1]
dy = [1, 0, -1 , 0]

# 방문 순서 아래 -> 왼쪽 -> 위 -> 오른쪽

def dfs(matrix, dn, dm):
    if 0 <= dn < n and 0 <= dm < m:
        if matrix[dn][dm] == 0:
            # 방문 처리
            matrix[dn][dm] = 1

            nn, nm = dn, dm
            for i in direc:
                nn = dn + dy[i]
                nm = dm + dx[i]
                dfs(matrix, nn, nm)
            return True
    else:
        return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(matrix, i, j):
            count += 1
print(count)
