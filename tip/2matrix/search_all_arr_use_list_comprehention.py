# 리스트 컴프리 헨션을 이용해 2차원 배열 특정 범위로 자르며 순회하기 2


# 2차원 배열은 슬라이싱을 할떄 
# 로우로 먼저 슬라이싱 하고
# 이를 이용해 컬럼 슬라이싱을 해야함

# 따라서 리스트 컴프리핸션을 이용해 슬라이싱한다
# for문을 이용해 로우를 먼저 슬라이싱하고 이를 받아 다시 슬라이싱하는 기법
# 매우 유용하니 꼭 기억핻줄것
y, x = map(int, input().split())

map_arr = []

for r in range(y):
    map_arr.append(list(input()))

ches_map = []

for r_idx in range(y - 7):
    for c_idx in range(x - 8):
        ches_map = [row[c_idx : c_idx + 8] for row in map_arr[r_idx : r_idx+ 8]]
        for c in ches_map:
            print(c)
        print()



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