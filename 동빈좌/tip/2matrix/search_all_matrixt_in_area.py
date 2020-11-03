# 리스트 컴프리 헨션을 이용해 2차원 배열 특정 범위로 자르며 순회하기 2


# 2차원 리스트 m x n
# 특정 범위 a x b (a < m, b < n)
# 로 나누어 전부 순회

y, x = map(int, input().split())

m = []

for r in range(y):
    m.append(list(input()))

cnt = 0
for r_idx in range(y - 7):
    for c_idx in range(x - 7):
        for r in range(r_idx, r_idx + 8):
            for c in range(c_idx, c_idx + 8):
                print(m[r][c], end='')
            print()
        cnt += 1
        print(cnt)
        print()

# 입력 예
# 10 10
#
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


a = ['a','b','c']

for i in a:
    i = 'x'
print(a)