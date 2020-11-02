def digit_sum(x):
    x = str(x)
    return sum(list(map(int, x)))

n = int(input())
arr = list(map(int, input().split()))

max_v = digit_sum(arr[0])
idx = 0
for i in range(1, n):
    if digit_sum(arr[i]) > max_v:
        max_v = digit_sum(arr[i])
        idx = i
print(arr[idx])