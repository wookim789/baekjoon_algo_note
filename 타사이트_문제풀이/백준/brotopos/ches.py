# 체스판 칠하기
import copy

y, x = map(int, input().split())

m = []

for r in range(y):
    m.append(list(input()))

# 8 x 8 영역을 전부 순회
# 좌측 상단 w or b 설정하여 칠해야 하는 수 설정
# min으로 갱신

# W B

# 2 for 로우 > 컬럼
result = int(1e9)
for r_idx in range(y - 7):
    for c_idx in range(x - 7):
        temp_arr = []
        for r in range(r_idx, r_idx + 8):
            temp_arr.append(m[r][c_idx : c_idx + 8])
        # 좌측 상단의 색을 변경하여 한번더 검사를 위해
        sec_temp_arr = copy.deepcopy(temp_arr)
        left_top = temp_arr[0][0]
        if left_top == 'W':
            sec_temp_arr[0][0] = 'B'
        else :
            sec_temp_arr[0][0] = 'W'

        left_first = ''
        befor = ''
        change_cnt = 0
        first_col = 0
        for r in range(8):
            for c in range(8):
                if left_first == '':
                   left_first = temp_arr[r][c]
                   befor = temp_arr[r][c]
                   first_col += 1
                   continue

                if first_col == 0:
                    if left_first == temp_arr[r][c]:
                        if temp_arr[r][c] == 'B':
                            temp_arr[r][c] = 'W'
                        else:
                            temp_arr[r][c] = 'B'
                        change_cnt += 1
                    first_col += 1
                    left_first = temp_arr[r][c]
                elif befor == temp_arr[r][c]:
                    if temp_arr[r][c] == 'B':
                        temp_arr[r][c] = 'W'
                    else:
                        temp_arr[r][c] = 'B'
                    change_cnt += 1
                befor = temp_arr[r][c]
            first_col = 0
        result = min(result, change_cnt)

        
        left_first = ''
        befor = ''
        change_cnt = 0
        first_col = 0
        for r in range(8):
            for c in range(8):
                if left_first == '':
                   left_first = sec_temp_arr[r][c]
                   befor = sec_temp_arr[r][c]
                   first_col += 1
                   continue

                if first_col == 0:
                    if left_first == sec_temp_arr[r][c]:
                        if sec_temp_arr[r][c] == 'B':
                            sec_temp_arr[r][c] = 'W'
                        else:
                            sec_temp_arr[r][c] = 'B'
                        change_cnt += 1
                    first_col += 1
                    left_first = sec_temp_arr[r][c]
                elif befor == sec_temp_arr[r][c]:
                    if sec_temp_arr[r][c] == 'B':
                        sec_temp_arr[r][c] = 'W'
                    else:
                        sec_temp_arr[r][c] = 'B'
                    change_cnt += 1
                befor = sec_temp_arr[r][c]
            first_col = 0
        result = min(result, change_cnt)
print(result)
# wbwbwbwbwb
# bwbwbwbwbw
# bwbwbwbwbw
# wbwbwbwbbw
# bwbwbwbwbw
# wbwbwbwbwb
# bwbwbwbwbw
# wbwbwbwbwb
# bwbwbwbwbw
# wbwbwbwbwb
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW


# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB