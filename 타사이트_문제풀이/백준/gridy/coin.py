# 동전 거슬러주기

n, result = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

answer = 0
for i in range(n - 1, -1, -1):
    if result == 0:
        break
    if coins[i] == result:
        answer += 1
        break
    elif coins[i] < result:
        answer += result // coins[i]
        result = result % coins[i]
print(answer)