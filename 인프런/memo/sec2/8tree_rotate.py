# 감나무 회전


# 2 (0, 1) 3
# 행 (왼쪽 오른쪽) 밀리는 칸수

n = int(input())
matr = []
for i in range(n):
    matr.append(list(map(int, input().split())))

m = int(input())
order = []
for i in range(m):
    order.append(list(map(int, input().split())))

# 회전명령 수행 -> 매트릭스 변경
for i in range(m):
    ridx, dirt, num = order[i][0] - 1, order[i][1], order[i][2]

    row = matr[ridx]
    tmp = [0] * n
    for i in range(n):
        if dirt != 0:
            tmp[(i + num) % n] = row[i]
        else:
            if i - num >= 0 :
                tmp[i - num] = row[i]
            else:
                tmp[i - num + n] = row[i]
    matr[ridx] = tmp
    row.clear()
    
# 모래시계 영역 sum
sidx = 0 
eidx = n - 1
result = 0
for i in range(n):
    
    if sidx < eidx - 1:
        result += sum(matr[i][sidx:eidx+1])
    elif sidx == eidx:
        result += sum(matr[i][sidx:eidx+1])
    else:
        result += sum(matr[i][eidx:sidx+1])

    sidx += 1
    eidx -= 1
print(result)