# 토마토 
# 1 256

# bfs 문제

from collections import deque
m, n = map(int, input().split())

que = deque()

arr_map = []
for i in range(n):
    arr_map.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        if arr_map[y][x] == 1:
            que.append([y, x])

while que:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    y, x = que.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and arr_map[ny][nx] == 0:
            arr_map[ny][nx] = arr_map[y][x] + 1
            que.append([ny, nx])

isTrue = False
result = -2
for i in arr_map:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)


