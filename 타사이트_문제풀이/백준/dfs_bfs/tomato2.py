# 토마토 3차원
import sys
m, n, h = map(int, sys.stdin.readline().rstrip().split())

def search_tomato_2d(h):
    global m, n, tomato_3d
    tomato_2d = tomato_3d[h]
    is_changed = 0
    for y in range(n):
        for x in range(m):
            if tomato_2d[y][x] > 0:
                # 주위 4방향 + 위 아래 익히기
                is_changed += change_arround(y, x, tomato_2d[y][x], h)
    return is_changed

def change_arround(y, x, cur_date, cur_h):
    global m, n, h, tomato_3d
    # 남 북 서 동
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    # 아래 위
    dh = [1, -1]
        
    is_changed = 0
    cur_tomato_2d = tomato_3d[cur_h]
    for i in range(4):
        if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n and cur_tomato_2d[y + dy[i]][x + dx[i]] == 0:
            cur_tomato_2d[y + dy[i]][x + dx[i]] = cur_date + 1
            is_changed += 1
    for h_idx in range(2):
        dif_2d = None
        if 0 <= cur_h + dh[h_idx] < h:
            dif_2d = tomato_3d[cur_h + dh[h_idx]]
            if dif_2d[y][x] == 0:
                dif_2d[y][x] = cur_date + 1
                is_changed += 1
    return is_changed

tomato_3d = []

for h_idx in range(h):
    tomato_2d = []
    for x in range(n):
        tomato_2d.append(list(map(int, sys.stdin.readline().rstrip().split())))
    tomato_3d.append(tomato_2d)

is_changed = 1
while is_changed != 0:
    is_changed = 0
    for h_idx in range(h):
        is_changed += search_tomato_2d(h_idx)
        
max_date = 0
is_fininsh = True

for h_idx in range(h):
    tomato_2d = tomato_3d[h_idx]
    for row in tomato_2d:
        if not 0 in row:
            max_date = max(max_date, max(row))
            continue
        else: 
            is_fininsh = False
            break

if is_fininsh:
    print(max_date - 1)
else:
    print(-1)
