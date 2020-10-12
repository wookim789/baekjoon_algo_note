# 스도쿠

# 계획 백트래킹의 핵심

# 브루트포스가 전부 다 순회하는거라면
# 백트래킹은 완전 탐색 도중에 실패한다면 특정 지점으로 다시 돌아가는 알고리즘이라 한다

# 스도쿠의 핵심은 0인 지점의 알맞은 숫자를 집어 넣는것

# 즉 검사할 대상은 0인 녀석들

# 조건
# 각 행에 0이 하나만 있다
# 각 열에 0이 하나만 있다
# 3x3으로 나눈 9개의 영역중에 하나의 블록에 0이 하나만 있다

# 위 세조건을 만족하면 0에 넣을 숫자를 알 수 있다

import sys
from collections import deque

sudoqu = []
zero_codi = deque()

for i in range(9):
    sudoqu.append(list(map(int, sys.stdin.readline().split())))

def search_zero():
    global sudoqu, zero_codi

    for row in range(9):
        for col in range(9):
            if sudoqu[row][col] == 0:
                codinate = (row, col)
                zero_codi.append(codinate)

def set_answer_in_row(codi):
    global sudoqu
    result = False
    row, col = codi[0], codi[1]

    if sudoqu[row].count(0) == 1:
        sudoqu[row][col] = get_corret_num('row', row)
        result = True
    return result

def set_answer_in_column(codi):
    global sudoqu
    result = False
    row, col = codi[0], codi[1]

    col_arr = []
    for row_idx in range(9):
        col_arr.append(sudoqu[row_idx][col])

    if  col_arr.count(0) == 1:
        sudoqu[row][col] = get_corret_num('col', col)
        result = True
    return result

def set_answer_in_block(codi):
    global sudoqu
    row, col = codi[0], codi[1]
    row_block, col_block = (row // 3) * 3, (col // 3) * 3
    block = [row[col_block : col_block + 3] for row in sudoqu[row_block : row_block + 3]]
    zero_cnt = 0
    for row_b in block:
        zero_cnt += row_b.count(0)

    if zero_cnt != 1:
        return False
    
    sudoqu[row][col] = get_corret_num('block', block)
    return True

def get_corret_num(sum_type, index):
    global sudoqu
    tot = 45
    result = 0
    if sum_type == 'row':
        result = tot - sum(sudoqu[index])
    elif sum_type == 'col':
        result = tot
        for row in range(9):
            result -= sudoqu[row][index]
    elif sum_type == 'block':
        result = tot
        block = index
        for b in block:
            result -= sum(b)
    return result

search_zero()

while len(zero_codi) > 0:
    codi = zero_codi.popleft()
    result = set_answer_in_row(codi)
    if not result:
        result = set_answer_in_column(codi)
    if not result:
        result = set_answer_in_block(codi)
    if not result:
        zero_codi.append(codi)
for s in sudoqu:
    for el in s:
        print(el, end =' ')
    print()


# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0

# 4 0 0 8 0 0 1 0 0
# 0 0 9 5 0 0 8 0 0 8
# 0 0 1 6 0 0 9 0 2 0
# 1 8 9 5 0 4 9 0 0 4
# 0 2 0 0 6 8 0 4 6 7
# 5 0 3 0 5 0 0 3 9 0
# 0 6 0 0 9 0 0 4 8 0
# 0 0 0 0 8 0 0 7 0 5


# 0 0 5 3 0 0 0 0 0
# 8 0 0 0 0 0 0 2 0
# 0 7 0 0 1 0 5 0 0 
# 4 0 0 0 0 5 3 0 0 
# 0 1 0 0 7 0 0 0 6
# 0 0 3 2 0 0 0 8 0
# 0 6 0 5 0 0 0 0 9
# 0 0 4 0 0 0 0 3 0
# 0 0 0 0 0 9 7 0 0 
