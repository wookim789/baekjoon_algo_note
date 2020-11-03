# 1 2      3               4                   5                 6                 7 8 9 10 11 12
# 1 (1,1)  (f(2) + 1, 1)   (f(3) +1, count    (f(4) + 1, count)  (f(5) + 1, count)


n = int(input())

dp = [0] * (n+2)

for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1
    if i % 2 ==0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 ==0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 ==0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[n])