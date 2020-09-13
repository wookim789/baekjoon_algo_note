n, k = map(int, input().split())


coins = []
for idx in range(n):
    coins.append(int(input()))


count = 0
for idx in range(n-1, 0, -1):
    if k == 0:
        break
    if k > coins[idx]:
        m, k = map(int, divmod(k, coins[idx]))
        count += m
print(count)



# 10 4790
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000