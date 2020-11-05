#격자판 최대합

n = int(input())
matr = []

result = 0

# 입력 받기 및 행합의 최대값 구하기
for i in range(n):
    row = list(map(int, input().split()))
    result = max(result, sum(row))
    matr.append(row)

# 열합의 최대값 구하기
for c in range(n):
    tot = 0
    for r in range(n):
        tot += matr[r][c]
    result = max(result, tot)

# 대각선 왼쪽 합 구하기
tot = 0
for idx in range(n):
    tot += matr[idx][idx]
result = max(result, tot)

# 대각선 오른쪽 합 구하기
tot = 0
for i in range(n):
    tot += matr[i][n -1 - i]
result = max(result, tot)

print(result)