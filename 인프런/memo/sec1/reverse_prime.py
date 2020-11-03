# 뒤집은 소수


ertos = []

def reverse(x):
    x = list(str(x))
    x.reverse()
    return int(''.join(x))

def isPrime(x):
    global ertos
    if ertos[x] == 1:
        print(x, end =' ')


n = int(input())
arr = list(map(int, input().split()))

reverse_arr = []

for i in arr:
    reverse_arr.append(reverse(i))

max_val = max(reverse_arr)
ertos = [0] * (max_val + 1)

for i in range(2, max_val + 1):
    if ertos[i] == 0:
        ertos[i] = 1
        for j in range(i, max_val + 1, i):
            if ertos[j] == 0:
                ertos[j] = 2

for r in reverse_arr:
    isPrime(r)