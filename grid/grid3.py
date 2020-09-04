# 어떤수 N이 1이 될 때까지 
# 최소 연산 횟수 구하기

# 연산 1 : N - 1 
# 연산 2 : N / K (단 나누어 떨어질때만 가능)

N, K = map(int, input().split())
result = 0
while N != 1:
    if K > 1 and N >= K and N % K == 0:
        N /= K
    else :
        N -= 1
    result += 1

print(result)
