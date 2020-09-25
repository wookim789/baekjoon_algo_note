# 체스판 칠하기
import copy
y, x = map(int, input().split())

map_arr = []

for r in range(y):
    map_arr.append(list(input()))

ches_map = []
result = int(1e9)
standard = ['W', 'B']
change_color = {'W' : 'B', 'B' : 'W'}

for r in range(y - 7):
    for c in range(x - 7):
        ches_map = [row[c : c + 8] for row in map_arr[r : r+ 8]]
        temp_map = copy.deepcopy(ches_map)
        for std in standard:
            cnt = 0
            for r_idx in range(8):
                for c_idx in range(8):
                    if c_idx == 0:
                        if std == ches_map[r_idx][c_idx]:
                            changed_color = change_color[ches_map[r_idx][c_idx]]
                            ches_map[r_idx][c_idx] = changed_color
                            cnt += 1
                        std = ches_map[r_idx][c_idx]
                    elif c_idx !=0 and ches_map[r_idx][c_idx] == ches_map[r_idx][c_idx - 1]:
                        ches_map[r_idx][c_idx] = change_color[ches_map[r_idx][c_idx]]
                        cnt += 1
            print(cnt)
            result = min(result, cnt)
            ches_map = temp_map
print(result)

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



# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW





















# for r_idx in range(y - 7):
#     for c_idx in range(x - 7):
#         temp_arr = []
#         for r in range(r_idx, r_idx + 8):
#             temp_arr.append(m[r][c_idx : c_idx + 8])
#         # 좌측 상단의 색을 변경하여 한번더 검사를 위해
#         sec_temp_arr = copy.deepcopy(temp_arr)
#         left_top = temp_arr[0][0]
#         if left_top == 'W':
#             sec_temp_arr[0][0] = 'B'
#         else :
#             sec_temp_arr[0][0] = 'W'

#         left_first = ''
#         befor = ''
#         change_cnt = 0
#         first_col = 0
#         for r in range(8):
#             for c in range(8):
#                 if left_first == '':
#                    left_first = temp_arr[r][c]
#                    befor = temp_arr[r][c]
#                    first_col += 1
#                    continue

#                 if first_col == 0:
#                     if left_first == temp_arr[r][c]:
#                         if temp_arr[r][c] == 'B':
#                             temp_arr[r][c] = 'W'
#                         else:
#                             temp_arr[r][c] = 'B'
#                         change_cnt += 1
#                     first_col += 1
#                     left_first = temp_arr[r][c]
#                 elif befor == temp_arr[r][c]:
#                     if temp_arr[r][c] == 'B':
#                         temp_arr[r][c] = 'W'
#                     else:
#                         temp_arr[r][c] = 'B'
#                     change_cnt += 1
#                 befor = temp_arr[r][c]
#             first_col = 0
#         result = min(result, change_cnt)

        
#         left_first = ''
#         befor = ''
#         change_cnt = 0
#         first_col = 0
#         for r in range(8):
#             for c in range(8):
#                 if left_first == '':
#                    left_first = sec_temp_arr[r][c]
#                    befor = sec_temp_arr[r][c]
#                    first_col += 1
#                    continue

#                 if first_col == 0:
#                     if left_first == sec_temp_arr[r][c]:
#                         if sec_temp_arr[r][c] == 'B':
#                             sec_temp_arr[r][c] = 'W'
#                         else:
#                             sec_temp_arr[r][c] = 'B'
#                         change_cnt += 1
#                     first_col += 1
#                     left_first = sec_temp_arr[r][c]
#                 elif befor == sec_temp_arr[r][c]:
#                     if sec_temp_arr[r][c] == 'B':
#                         sec_temp_arr[r][c] = 'W'
#                     else:
#                         sec_temp_arr[r][c] = 'B'
#                     change_cnt += 1
#                 befor = sec_temp_arr[r][c]
#             first_col = 0
#         result = min(result, change_cnt)
# print(result)
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