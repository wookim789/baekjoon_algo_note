maze =[[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]	#32
maze =[[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]	#24
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]	#22
maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]	#10




# 현재 방향 받으면 왼쪽 방향 리턴
def turn_left(cur_dir):
    left = 0
    if cur_dir == 0:
        left = 3
    else :
        left = cur_dir - 1
    return left

# 현재 방향 받으면 오른쪽쪽 방향 리턴
def turn_right(cur_dir):
    right = 0
    if cur_dir == 3:
        right = 0
    else :
        right = cur_dir + 1
    return right

# 현재 좌표에서 해당 방향 및 왼쪽 방향 이동 가능한지 확인
def check_point(y,x, cur_dir, maze, n):
    dire = [0, 1, 2, 3]
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    
    fy = y + dy[cur_dir]
    fx = x + dx[cur_dir]
    check = []
    if (0 <= fx <= n and 0 <= fy <= n) and maze[fy][fx] == 1:
        check.append(False)
    else:
        check.append(True)
    
    # 왼쪽으로 회전
    left_dir = turn_left(cur_dir)
    
    lx = x - dx[left_dir]
    ly = y - dy[left_dir]
    if (0 <= lx <= n and 0 <= ly <= n) and maze[ly][lx] == 1:
        check.append(False)
    else:
        check.append(True)
    # 앞방향 및 왼쪽 방향으로 이동 가능 여부 리턴
    return check


# maze = 
# [[0, 1, 0, 1], 
# [0, 1, 0, 0], 
# [0, 0, 0, 0], 
# [1, 0, 1, 0]]	#10

answer = 0
n = len(maze) - 1
#북, 동, 남, 서
dire = [0, 1, 2, 3]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

x, y = 0, 0
# 남쪽 바라보고 시작
cur_dir = 2 
# 목적지 도착까지 반복
while x != n and y != n:
    f_l = check_point(y, x, cur_dir, maze, n)
    # 앞 0 왼 x
    print(y, x, cur_dir, f_l, n)
    if f_l[0] and not f_l[1]:
        print(dx[cur_dir], dy[cur_dir])
        if 0 <= x + dx[cur_dir] <= n and 0 <= y + dy[cur_dir] <= n:
            x = x + dx[cur_dir]
            y = y + dy[cur_dir]
            print(y, x, cur_dir, f_l, n)
        # foward
        answer += 1
    # 앞 0 왼 0 -> 왼쪽 회전
    # 앞 x 왼 0 -> 왼쪽 회전
    elif (f_l[0] and f_l[1]) or (not f_l[0] and f_l[1]):
        cur_dir = turn_left(cur_dir)
        # if 0 <= x + dx[cur_dir] <= n:
            # x = x + dx[cur_dir]
        # if 0 <= y + dy[cur_dir] <= n:
            # y = y + dy[cur_dir]
        # foward
    # 앞 x 왼 x -> 오른쪽 회전
    elif not f_l[0] and not f_l[1]:
        cur_dir = turn_right(cur_dir)