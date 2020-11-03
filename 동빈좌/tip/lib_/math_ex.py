import math

# 팩토리얼 
print(math.factorial(5))

# 팩토리얼로 순열 구하기

def pumpu(n, r):
    return int(math.factorial(n) / math.factorial(n-r))

print(pumpu(3,2))

# 팩토리얼로 조합 구하기

def combi(n, r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

print(combi(3,2))


# 최대공약수

print(math.gcd(21, 14))