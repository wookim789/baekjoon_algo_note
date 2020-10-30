import sys

t = int(input())
T = 1
for _ in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr[s-1 : e])
    print('#', end = '')
    print(T, arr[k - 1])
    T += 1