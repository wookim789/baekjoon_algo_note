# 소수 구하기
# 2
# 30분 128mb

# m이상 n 이하의 소수를 모두 구하시오
from math import sqrt
m, n = map(int, input().split())

# 소수 판별
# 판별하려는 k 
# k의 제곱은을 구함 j = int(math.sqrt(k))
# 1 부터 j까지 k를 나누어서 떨어지면 
# 소수라 판별

def eratosthenes(n):
    array = [True for i in range(n + 1)]
    for i in range(2, int(sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
                
    return array

demical_arr = eratosthenes(n)

for i in range(m, n + 1):
    if demical_arr[i]:
        print(i, end =' ')