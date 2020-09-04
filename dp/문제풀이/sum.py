# 1부터 n까지 더하기

def sum(n):
    if n >= 1:
        return n + sum(n-1)
    elif n == 0:
        return 0

print(sum(10))