key, lock = [[0, 0, 0],[1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# arr = [[0, 0, 0],[1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# key
print(len(key))
print(len(key[0]))

k = len(key[0])
# lock
n = len(lock[1])

# 정사각형을 3배의 큰 정사각 중앙에 위치

new_arr = [[0] * 3 * n for _ in range(3 * n)]

for i in range(n):
    new_arr[n+i][3:6] = lock[i]


def is_correct(lock):
    # 중앙 자물쇠 칸이 전부 1로 이루어져있고
    result = True
    for y in range(n, 2*n):
        for x in range(n, 2*n):
            if lock[y][x] != 1:
                result = False
    return result


def rotate_90(m):
    N = len(m)
    # 2차원 배열은 컴프리 헨션으로 선언해야 행마다 새 객체로 이루어짐
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


def print_dir(arr):
    for i in arr:
        print(i)
    print()

def solution():
    global n, k, new_arr, key
    for y in range(3*n - k):
        for x in range(3*n - k):
            for i in range(4):
                sum_arr(y,x)
                if not is_correct(new_arr):
                    sub_arr(y,x)
                    key = rotate_90(key)
                else:
                    print('-------sum  -------')
                    print_dir(new_arr)
                    return True
                # print_dir(new_arr)
    return False

def sum_arr(y, x):
    global new_arr, k
    for ky in range(k):
        na = new_arr[y + ky][x : x + k]
        ka = key[ky]
        sum_k = [l + s for l, s in zip(na,ka)]
        new_arr[y + ky][x : x + k] = sum_k
    return 

def sub_arr(y, x):
    global new_arr, k
    for ky in range(k):
        na = new_arr[y + ky][x : x + k]
        ka = key[ky]
        sub_k = [l - s for l, s in zip(na,ka)]
        new_arr[y + ky][x : x + k] = sub_k
    return 

print(solution())
# print_dir(new_arr)