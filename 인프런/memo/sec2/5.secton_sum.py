n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
a, b = 0, 0

while True:
    if a > n or b > n:
        break
    sum_arr = sum(arr[a:b])
    if sum_arr == m:
        result += 1
        b += 1
    elif sum_arr > m and a < b:
        a += 1
    elif sum_arr > m and a == b:
        b += 1
    elif sum_arr < m:
        b += 1

print(result)