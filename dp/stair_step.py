# 계단을 오른다
# N번째 계단을 
# 1칸 혹은 2칸으로 오를수 있는 
# 모든 경우수를 구하시오

n = int(input())

dp = [0] * (n+2)

dp[1], dp[2] = 1,2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])