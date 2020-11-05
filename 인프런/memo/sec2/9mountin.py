# 봉우리

n = int(input())
matr = []
matr.append([0] * (n+2))
for i in range(n):
    tmp = [0]
    tmp += list(map(int, input().split()))
    tmp.append(0)
    matr.append(tmp)
matr.append([0] * (n+2))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0
for r in range(1, n + 1):
    for c in range(1, n + 1):
        for i in range(4):
            next_r = r + dx[i]
            next_y = c + dy[i]
            if matr[r][c] <= matr[next_r][next_y]:
                break
        else:
            result += 1

print(result)