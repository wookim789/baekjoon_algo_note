# n_queen

import sys
sys.setrecursionlimit(200000)
n = int(input())
w_list = []
matrix = [[0] * n for _ in range(n)]

def set_danger_zone(r, c, is_recover):
    global matrix
    num = -1
    t_m = matrix[r][c]
    if is_recover:
        num = 1
    
    for tmp_r in range(n):
        matrix[tmp_r][c] += num
    
    for tmp_c in range(n):
        matrix[r][tmp_c] += num
    
    tmp_r = r
    tmp_c = c

    while tmp_r >= 1 and tmp_c >= 1:
        tmp_r -= 1
        tmp_c -= 1
        matrix[tmp_r][tmp_c] += num
    
    tmp_r = r
    tmp_c = c

    while tmp_r < n - 1 and tmp_c >= 1:
        tmp_r += 1
        tmp_c -= 1
        matrix[tmp_r][tmp_c] += num
    
    tmp_r = r
    tmp_c = c

    while tmp_r >= 1 and tmp_c < n - 1:
        tmp_r -= 1
        tmp_c += 1
        matrix[tmp_r][tmp_c] += num

    tmp_r = r
    tmp_c = c

    while tmp_r < n - 1 and tmp_c < n - 1:
        tmp_r += 1
        tmp_c += 1
        matrix[tmp_r][tmp_c] += num
    
    matrix[r][c] = t_m + num

def select_point(tmp_w_list):
    global matrix, w_list

    if len(tmp_w_list) == n:
        w_list.append(tmp_w_list)
        (tr, tc) = tmp_w_list.pop()
        set_danger_zone(tr, tc, True)
        return
    
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 0:
                set_danger_zone(r, c, False)
                for m in matrix:
                    print(m)
                print()
                tmp_w_list.append((r, c))
                select_point(tmp_w_list)

    if tmp_w_list:
        (tr, tc) = tmp_w_list.pop()
        set_danger_zone(tr, tc, True)

select_point([])
print(w_list)
print(len(w_list))