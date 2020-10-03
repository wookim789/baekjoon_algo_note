# 스도쿠

import sys
sys.setrecursionlimit(200000000)

s_map = []

for i in range(9):
    s_map.append(list(map(int, sys.stdin.readline().split())))

is_done = False

def check_zero_in_row():
    global s_map
    if check_done():
        return 

    for r_idx in range(9):
        if s_map[r_idx].count(0) == 1:
            col_idx = s_map[r_idx].index(0)
            s_map[r_idx][col_idx] = 45 - sum(s_map[r_idx])

    check_zero_in_col()
    
def check_zero_in_col():
    global s_map
    tmp_col_arr = []
    result = False

    if check_done():
        return 

    for i in range(9):
        tmp_col_arr.append([row[i] for row in s_map[:]])

    for r_idx in range(9):
        if tmp_col_arr[r_idx].count(0) == 1:
            col_idx = tmp_col_arr[r_idx].index(0)
            tmp_col_arr[r_idx][col_idx] = 45 - sum(tmp_col_arr[r_idx])
            result = True
    tmp = []
    for i in range(9):
        tmp.append([row[i] for row in tmp_col_arr[:]])
    s_map = tmp

    if result:
        check_zero_in_row()
    else:
        check_block()

def check_block():
    global s_map
    smal_map = []
    
    if check_done():
        return

    for r_idx in range(0, 9, 3):
        for c_idx in range(0, 9, 3):
            smal_map = [row[c_idx : c_idx + 3] for row in s_map[r_idx : r_idx+ 3]]
            tot = 45
            t_ridx = 0
            t_cidx = 0
            cnt = 0
            point = 0
            for ri in range(3):
                for ci in range(3):
                    if smal_map[ri][ci] == 0:
                        point = (ri, ci)
                        cnt += 1
                    tot -= smal_map[ri][ci]
            
            t_ridx += r_idx
            t_cidx += c_idx
            if cnt == 1:
                s_map[t_ridx + point[0]][t_cidx + point[1]] = tot

    if check_done():
        return
    else:
        check_zero_in_row()


def check_done():
    global s_map, is_done

    for r in s_map:
        if sum(r) != 45:
            is_done = False
            return is_done
    is_done = True
    return is_done

check_zero_in_row()
for i in s_map:
    for j in i:
        print(j, end=' ')
    print()
