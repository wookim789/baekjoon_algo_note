# 피버나치 수열
# 점화식 
# a(n) = a(n - 1) + a(n -2) (n > 2)
# 1 1 2 3 5 8 13 21 ...
# 이렇게 점화식으로 표현되면 재귀함수적으로 구현하기 편함

arr = [1,1]
def fivo(n):
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n-1]
print(fivo(100))


d = [0] * 105
def fivo2(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fivo2(x - 1) + fivo2(x-2)
    return d[x]
print(fivo2(100))


d = [0] * 105
def fivo3(x):
    print('f('+str(x)+')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fivo3(x-1) + fivo3(x-2)
    return d[x]
fivo3(10)