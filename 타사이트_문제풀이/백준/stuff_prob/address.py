# 단지번호붙이기 2667

# dfs로 모든 단지 순회
n = 7
map_tot = [[0,1,1,0,1,0,0],
            [0,1,1,0,1,0,1],
            [1,1,1,0,1,0,1],
            [0,0,0,0,1,1,1],
            [0,1,0,0,0,0,0],
            [0,1,1,1,1,1,0],
            [0,1,1,1,0,0,0]]
# print(map_tot)


# n = int(input())
# map_tot = []
# for i in range(n):
#     map_tot.append(list(map(int, input())))

visited = [[False] * n for _ in range(n)]
result = []

def dfs(y,x, visited, map_tot, count):
    if map_tot[y][x] == 0:
        return count
    if not visited[y][x]:
        visited[y][x] = True
        count += 1
        # 아래, 오른쪽, 위, 왼쪽 4방향 재귀
        if  y < n - 1:
            count = dfs(y + 1, x, visited, map_tot, count)
        if x < n - 1:
            count = dfs(y, x + 1, visited, map_tot, count)
        if 1 <= y:
            count = dfs(y - 1, x, visited, map_tot, count)
        if 1 <= x :
            count = dfs(y, x - 1, visited, map_tot, count)
    return count

for y in range(n):
    for x in range(n):
        count = dfs(y,x, visited, map_tot, 0)
        if  count > 0:
            result.append(count)
        
result.sort()
print(len(result))
for i in result:
    print(i)