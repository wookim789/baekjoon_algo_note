# 분해합

# x 
# x = a + b + c + abc

# x = a(100 + 1) + b(10 + 1) + 2c


# 1 <= n <= 1,000,000

n = int(input())

result = {}
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        equation = 100001*a + 10001*b + 1001*c + 101*d+ 11*e +2*f
                        answer = 100000*a + 10000*b + 1000*c + 100*d+ 10*e +1*f

                        if equation <= 1000000:
                            if not equation in result:
                                result[equation] = answer
                            else:
                                result[equation] = min(result[equation], answer)

if n in result:
    print(result[n])
else:
    print(0)