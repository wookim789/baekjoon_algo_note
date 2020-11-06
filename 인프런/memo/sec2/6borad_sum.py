#격자판 최대합

n = int(input())

result = 0

matr = [list(map(int, input().split())) for _ in range(n)]

# 각각의 행 열의 최대합 구하기
for i in range(n):
    sum_row = sum_col = 0
    for j in range(n):
        sum_row += matr[i][j]
        sum_col += matr[j][i]
        result = max(result, sum_row, sum_col)

# 대각선 왼쪽, 오른쪽 합 중 최대값 구하기
sum_left = sum_right = 0
for idx in range(n):
    sum_left += matr[idx][idx]
    sum_right += matr[idx][n - 1 - idx]
    result = max(result, sum_left, sum_right)
print(result)