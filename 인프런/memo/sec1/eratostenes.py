# 에라토스테네스의 체

n = int(input())

# 소수 : 약수가 자기자신과 1뿐인 수 다른 수로 나누어 떨어지지 않는 수

# 기억나는 건 DP 테이블을 사용하는것 : 메모이제이션
erato = [0] * (n + 1)

cnt = 0
for i in range(2, n + 1):
    if erato[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            erato[j] = 1

print(cnt)



cnt = 0 

while n % 2 == 0:
    n //= 2
    cnt += 1
    print(n)
print(cnt)

