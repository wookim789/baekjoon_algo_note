# 유기농 배추
# 1 512mb


from collections import deque

case_list = list()
# case = int(input())
# for i in range(case):
#     temp = dict()
#     m, n, k = map(int, input().split())
#     arr_map = [[0] * m for _ in range(n)]
#     for i in range(k):
#         x, y = map(int, input().split())
#         arr_map[y][x] = 1
#     temp['m'] = m
#     temp['n'] = n
#     temp['k'] = k
#     temp['arr_map'] = arr_map
#     case_list.append(temp)
# temp1 = dict()
# temp1['m'] = 10
# temp1['n'] = 8
# temp1['k'] = 17
# temp1['arr_map'] = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                     [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
#                     [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
#                     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# case_list.append(temp1)

# temp1 = dict()
# temp1['m'] = 10
# temp1['n'] = 10
# temp1['k'] = 1
# temp1['arr_map'] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# case_list.append(temp1)


from collections import deque

case_list = list()
case = int(input())
for i in range(case):
    temp = dict()
    m, n, k = map(int, input().split())
    arr_map = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr_map[y][x] = 1
    temp['m'] = m
    temp['n'] = n
    temp['k'] = k
    temp['arr_map'] = arr_map
    case_list.append(temp)
def print_map(map_data):
    for i in map_data:
        print(i)

def bfs(y, x, arr_map, m, n):
    que = deque()
    result = False
    if arr_map[y][x] == 1:
        # que에 적재
        que.append(tuple([y, x]))
        result = True
    # 큐가 빌때까지
    while que:
        # (y, x)
        codi_tup = que.popleft()
        dy = codi_tup[0]
        dx = codi_tup[1]
        if arr_map[dy][dx] == 1:
            # 방문 처리
            arr_map[dy][dx] = 0
            result = True
            # 오른쪽 아래, 왼쪽, 위 순으로 찾기
            if dx < m-1:
                que.append(tuple([dy, dx + 1]))
            if dy < n-1:
                que.append(tuple([dy + 1, dx]))
            if dx > 0:
                que.append(tuple([dy, dx -1]))
            if dy > 0:
                que.append(tuple([dy - 1, dx]))
    return result

for dic in case_list:
    n = dic['n']
    m = dic['m']
    arr_map = dic['arr_map']
    count = 0
    for y in range(n):
        for x in range(m):
            # bfs 탐색하여 영역 개수 세기
            if bfs(y, x, arr_map, m, n):
                count += 1
    print(count)


# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5



