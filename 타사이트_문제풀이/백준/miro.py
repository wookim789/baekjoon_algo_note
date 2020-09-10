# 미로 탐색
# 1 192 

# n,m으로 이동할 최소 칸수

# bfs 문제 -> 떙. dfs문제 -> 땡 bfs문제 ㅋㅋ;;




# n, m = 4, 6
# arr_map =  [[1, 0, 1, 1, 1, 1],
#             [1, 0, 1, 0, 1, 0],
#             [1, 0, 1, 0, 1, 1],
#             [1, 1, 1, 0, 1, 1]]
# n,m = 2, 25
# arr_map = [[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1],
#            [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]]
# n,m =7, 7
# arr_map =  [[1,0,1,1,1,1,1],
#             [1,1,1,0,0,0,1],
#             [1,0,0,0,0,0,1],
#             [1,0,0,0,0,0,1],
#             [1,0,0,0,0,0,1],
#             [1,0,0,0,0,0,1],
#             [1,1,1,1,1,1,1]]

# n,m =5, 5
# arr_map =  [[1,0,1,1,1],
#             [1,1,1,0,1],
#             [1,0,0,1,1],
#             [1,0,0,1,0],
#             [1,1,1,1,1]]



arr_map = []
n, m = map(int, input().split())
for x in range(n):
    data = input()
    temp = list()
    for y in data:
        temp.append(int(y))
    arr_map.append(temp)

from collections import deque

que = deque()

que.append(tuple([0, 0, 0]))
while que:
    codi = que.popleft()

    dy = codi[0]
    dx = codi[1]
    temp = codi[2]

    if dy == n-1 and dx == m-1:
        temp += 1
        print(temp)
        break

    if arr_map[dy][dx] == 1:
        arr_map[dy][dx] = 0
        temp += 1

        if dx < m - 1:
            que.append(tuple([dy, dx + 1, temp]))
        if dy < n - 1:
            que.append(tuple([dy + 1, dx, temp]))
        if dx > 0:
            que.append(tuple([dy, dx - 1, temp]))
        if dy > 0 :
            que.append(tuple([dy - 1, dx, temp]))





