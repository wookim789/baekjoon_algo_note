
map_size = list(map(int, input().split())) # n x m

spot_direction = list(map(int, input().split())) # (x, y, direction) ex) (1,1,0) = (1,1)위치의 방향은 북

map_data = []

# 이동 칸 수 
count = 1

while True:
    input_str = input()
    if input_str != 'end':
        map_data.append(list(map(int, input_str.split())))
    else:
        break


# 입력 확인


# 0 1 2 3 : 북 동 남 서
# 회전 함수
def rotate_direction(direction):
    result = 0
    if direction == 0:
        result = 3
    else:
        result = direction - 1
    return result

# 바다인지 판별
def check_is_sea(curent_spot, direction):
    print(curent_spot)
    global map_size
    dx, dy = 0, 0
    if direction == 0:
        dx = -1
    elif direction == 1:
        dy = 1
    elif direction == 2:
        dx = 1
    elif direction == 3:
        dy = -1
    result = False
    if curent_spot[0] + dx >= 0 and curent_spot[1] + dy >= 0:
        check_spot = [curent_spot[0] + dx, curent_spot[1] + dy]
        if check_spot[0] < map_size[0] and check_spot[1] < map_size[1]:
            if map_data[check_spot[0]][check_spot[1]] == 1:
                result = True
        else:
            result = True
    else:
        result = True
    return result

# 들렀던 곳인지 판별
def check_have_bean_place(spot):
    result = False
    dx, dy = 0, 0
    if direction == 0:
        dx = -1
    elif direction == 1:
        dy = 1
    elif direction == 2:
        dx = 1
    elif direction == 3:
        dy = -1

    if map_data[spot[0]+ dx][spot[1]+ dy] == 9:
        result = True
    return result
    
# 이동시 방문 처리
def count_place(spot, direction):
    global count
    dx, dy = 0, 0
    if direction == 0:
        dx = -1
    elif direction == 1:
        dy = 1
    elif direction == 2:
        dx = 1
    elif direction == 3:
        dy = -1

    spot = [spot[0] + dx, spot[1] + dy] 
    if map_data[spot[0]][spot[1]] != 9:
        map_data[spot[0]][spot[1]] = 9
        count += 1
    return spot

# 현재 방향의 뒤방향으로 전환
def back_step(direction):
    result = 0
    if direction == 0:
        result = 2
    elif direction == 1:
        result = 3
    elif direction == 2:
        result = 0
    elif direction == 3:
        result = 1
    return result

direction = list(spot_direction)[2]
spot = list(spot_direction)[0:2]
rotate_count = 0
map_data[spot[0]][spot[1]] = 9
while True:
    direction = rotate_direction(direction)
    rotate_count += 1
    
    if check_is_sea(spot, direction): # 바다라면
        if rotate_count < 4: # 처음방향이 아니라면
            continue
        else: # 처음 방향이면
            rotate_count = 0
            back_direction = back_step(direction) # 처음방향의 뒤로 방향 재설정
            if check_is_sea(spot, back_direction): # 뒤 방향이 바다라면
                break
            else: # 땅이라면
                spot = count_place(spot, back_direction)
    else: # 바다가 아니라면
        if check_have_bean_place(spot): #들린적이 있다면
            continue
        else:
            spot = count_place(spot, direction)
            rotate_count = 0

print(count)