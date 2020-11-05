# 사과나무

n = int(input())

matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))


center = int(n / 2)

sidx, eidx = 0, 1

result = 0
for i in range(n):
    result += sum(matr[i][center + sidx : center + eidx])
    if i < center: # 전반
        sidx -= 1
        eidx += 1
    else: # 후반
        sidx += 1
        eidx -= 1
print(result)

