# 01타일

# dp 문제

# 점화식

# An = A(n-1) + A(n-2)

N = int(input())

d = []

d.append(1)
d.append(2)

for i in range(N):
    if i > 1:
        d.append( (d[i-1] + d[i-2]) % 15746 )


print(d[N-1])