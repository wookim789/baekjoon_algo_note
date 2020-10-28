# 정수 삼각형

n = int(input())

tri = []
dp_table = [[0] * i for i in range(1, n + 1)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    tri.append(tmp)

dp_table[0][0] = tri[0][0]

# 양 끝은 전 항의 양끝으로 바로 더함
# 중간 값들은 max를 이용해 더 큰값으로 저장

for i in range(1, len(dp_table)):
    j = len(dp_table[i])
    dp_table[i][0] = dp_table[i-1][0] + tri[i][0]
    dp_table[i][j - 1] = dp_table[i-1][j - 2] + tri[i][j-1]

    for idx in range(1, j - 1):
        dp_table[i][idx] = max(dp_table[i-1][idx - 1] + tri[i][idx], dp_table[i-1][idx] + tri[i][idx])

result = 0
for i in dp_table:
    for j in i:
        result = max(result, j)
print(result)