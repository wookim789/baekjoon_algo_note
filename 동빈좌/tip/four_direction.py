
# 북 동 남 서
direction = [0, 1, 2, 3]

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 현재 방향
cur_direction = 1 # 동

x, y = map(int, input().split())

# 현재 방향으로 이동하는 로직
nx = x + dx[cur_direction]
ny = y + dy[cur_direction]

# 현재 방향 반대방향으로 이동하는 로직
nx = x - dx[cur_direction]
ny = y - dy[cur_direction]