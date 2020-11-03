# 주사위 게임
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

result = []
for r in arr:
    if r[0] == r[1] and r[0] == r[2]:
        result.append(10000 + r[0] * 1000)
    elif r[0] != r[1] and r[0] != r[2] and r[1] != r[2]:
        result.append(max(r) * 100)
    else:
        tmp = 0
        if r.count(r[0]) == 2:
            tmp = r[0]
        else:
            tmp = r[1]
        result.append(1000 + tmp * 100)
print(max(result))
