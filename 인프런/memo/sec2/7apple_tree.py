# 사과나무

n = int(input())

matr = [list(map(int, input().split())) for _ in range(n)]

center = n // 2
sidx = eidx = center

result = 0
for i in range(n):
    result += sum(matr[i][sidx : eidx + 1])
    if i < center: # 전반
        sidx -= 1
        eidx += 1
    else: # 후반
        sidx += 1
        eidx -= 1
print(result)

