# 토마토 3차원
import sys
from collections import deque

# bfs 1인 지점 큐에 저장
def bfs():
    global tmt_3d, tgt

    if not tgt:
        return -1

    while tgt:
        codi = tgt.popleft()
        h, y, x = codi[0], codi[1], codi[2]
        check_around(h, y, x)

def check_around(cur_h, cur_y, cur_x):
    global tmt_3d, m, n, h, tgt

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dh = [1, -1]
    tmt_2d = tmt_3d[cur_h]
    cur_date = tmt_2d[cur_y][cur_x]

    for xy_idx in range(4):
        x = cur_x + dx[xy_idx]
        y = cur_y + dy[xy_idx]
        if 0 <= x < m and 0 <= y < n:
            if tmt_2d[y][x] == 0 or tmt_2d[y][x] > cur_date + 1:
                tmt_2d[y][x] = cur_date + 1
                tgt.append([cur_h, y, x])
    for h_idx in range(2):
        d_h = cur_h + dh[h_idx]
        if 0 <= d_h < h:
            if  tmt_3d[d_h][cur_y][cur_x] == 0 or tmt_3d[d_h][cur_y][cur_x] > cur_date + 1:
                tmt_3d[d_h][cur_y][cur_x] = cur_date + 1
                tgt.append([d_h, cur_y, cur_x])

def print_max_date():
    global tmt_3d
    max_date = 0
    for h_idx in range(h):
        tmt_2d = tmt_3d[h_idx]
        for row in tmt_2d:
            if 0 in row:
                return -1
            max_date = max(max_date, max(row))
    return max_date - 1

m, n, h = map(int, sys.stdin.readline().rstrip().split())

tmt_3d = []
tgt = deque()

for h_idx in range(h):
    tmt_2d = []
    for r in range(n):
        tmt_row = list(map(int, input().split()))
        col_list = []
        for c_idx in range(m):
            if tmt_row[c_idx] == 1:
                col_list.append(c_idx)
        for c in col_list:
                tgt.append([h_idx, r, c])
        tmt_2d.append(tmt_row)
    tmt_3d.append(tmt_2d)

bfs()
print(print_max_date())

# for tmt_2d in tmt_3d:
#     for row in tmt_2d:
#         print(row)




























# def search_tomato_2d(h):
#     global m, n, tomato_3d
#     tomato_2d = tomato_3d[h]
#     is_changed = 0
#     for y in range(n):
#         for x in range(m):
#             if tomato_2d[y][x] > 0:
#                 # 주위 4방향 + 위 아래 익히기
#                 is_changed += change_arround(y, x, tomato_2d[y][x], h)
#     return is_changed

# def change_arround(y, x, cur_date, cur_h):
#     global m, n, h, tomato_3d
#     # 남 북 서 동
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     # 아래 위
#     dh = [1, -1]
        
#     is_changed = 0
#     cur_tomato_2d = tomato_3d[cur_h]
#     for i in range(4):
#         if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n and cur_tomato_2d[y + dy[i]][x + dx[i]] == 0:
#             cur_tomato_2d[y + dy[i]][x + dx[i]] = cur_date + 1
#             is_changed += 1
#     for h_idx in range(2):
#         dif_2d = None
#         if 0 <= cur_h + dh[h_idx] < h:
#             dif_2d = tomato_3d[cur_h + dh[h_idx]]
#             if dif_2d[y][x] == 0:
#                 dif_2d[y][x] = cur_date + 1
#                 is_changed += 1
#     return is_changed

# tomato_3d = []

# for h_idx in range(h):
#     tomato_2d = []
#     for x in range(n):
#         tomato_2d.append(list(map(int, sys.stdin.readline().rstrip().split())))
#     tomato_3d.append(tomato_2d)

# is_changed = 1
# while is_changed != 0:
#     is_changed = 0
#     for h_idx in range(h):
#         is_changed += search_tomato_2d(h_idx)
        
# max_date = 0
# is_fininsh = True

# for h_idx in range(h):
#     tomato_2d = tomato_3d[h_idx]
#     for row in tomato_2d:
#         if not 0 in row:
#             max_date = max(max_date, max(row))
#             continue
#         else: 
#             is_fininsh = False
#             break

# if is_fininsh:
#     print(max_date - 1)
# else:
#     print(-1)
 