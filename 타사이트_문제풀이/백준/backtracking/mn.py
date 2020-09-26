# n과 m

from itertools import product

n, m = map(int, input().split())


arr = []
for i in range(1, n + 1):
    arr.append(str(i))

p = sorted(list(set(product(arr, repeat=m))))

for t in p:
    print(' '.join((list(t))))

