from itertools import combinations

n, m = map(int, input().split())

arr = list(map(int, input().split()))


c = list(map(list, combinations(arr, 3)))

result = 0
for i in c:
    s = sum(i)
    if s == m:
        result = s
        break
    elif m > s:
        result = max(result, s)

print(result)