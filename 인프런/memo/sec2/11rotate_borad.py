# 격자판 회문수

n = 7
matr = [list(map(int, input().split())) for _ in range(n)]
result = 0
for r in matr:
    for i in range(n - 5 + 1):
        tmp = r[i:i+5]
        if r[i:i+5] == tmp[::-1]:
            result += 1

for cidx in range(7):
    for rs_idx in range(n - 5 + 1):
        s = []
        for ridx in range(rs_idx, rs_idx + 5):
            s.append(matr[ridx][cidx])
        tmp = s
        if s == tmp[::-1]:
            result += 1
print(result)