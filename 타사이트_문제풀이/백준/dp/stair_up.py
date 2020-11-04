n = int(input())

cost = []
for _ in range(n):
    cost.append(int(input()))

if len(cost) == 1:
    print(cost[0])
elif len(cost) == 2:
    print(cost[1] + cost[0])
else:
    dp = [0] * (n)
    dp[0] = cost[0]
    dp[1] = max(cost[0] + cost[1], cost[1])
    # dp[2] = max(cost[2] + cost[0], cost[2] + cost[1])

    for i in range(2, n):
        dp[i] = max(cost[i] + cost[i - 1] + dp[i - 3], cost[i] + dp[i-2])

    print(dp[-1])

