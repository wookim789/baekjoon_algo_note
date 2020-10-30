n = int(input())

arr = list(map(int, input().split()))

avg = round(sum(arr)/n)

arr = [ i - avg for i in arr]

rep = int(1e9)
is_minus = False
idx = 0
for i in range(n):
    if rep > abs(arr[i]):
        if arr[i] < 0:
            is_minus = True
        else:
            is_minus = False
        rep = abs(arr[i])
        idx = i
    elif rep == abs(arr[i]) and is_minus and arr[i] > 0:
        idx = i
        is_minus = False
print(avg, idx + 1)