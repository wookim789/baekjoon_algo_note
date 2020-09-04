import operator

if __name__ == "__main__":
        # 회전 함수
    def rotate(direction):
        result = 0
        if direction == 0:
            result = 3
        else:
            result = direction - 1
        return result
    
    map_size = list(map(int ,input().split()))
    state = list(map(int ,input().split()))

    map_data = []
    map_row = input()
    while map_row != 'end':
        map_data.append(list(map(int, map_row.split())))
        map_row = input()


    directions = [0, 1, 2, 3]
    step = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    traces = []

    # 최초 위치 추가
    traces.append([state[0], state[1]])
    current_loc = [state[0], state[1]]
    current_dir = state[2]
    rotate_num = 0

    while True:
        next_loc = list(map(operator.add, current_loc, step[current_dir]))
        print(next_loc)
        if next_loc in traces:
            current_dir = rotate(current_dir)
            rotate_num += 1
            continue
        elif map_data[next_loc[0]][next_loc[1]] != 1 and rotate_num < 4:
            traces.append(next_loc)
            current_loc = next_loc
            rotate_num = 0
        elif rotate_num == 4:
            rotate_num = 0
            gap = map(operator.sub, current_loc, next_loc)
            back_loc = list(map(operator.add, current_loc, gap))
            if map_data[back_loc[0]][back_loc[1]] != 1:
                current_loc = back_loc
                traces.append(current_loc)
            else:
                break
        current_dir = rotate(current_dir)
        rotate_num += 1
    print(len(traces))

