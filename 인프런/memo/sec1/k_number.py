import sys

t = int(input())
result = []
for _ in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr[s-1 : e])
    result.append(arr[k - 1])

t = 1
for i in result:
    print('#', end='')
    print(t, i)
    t += 1