# 증가 수열
from collections import deque

n = int(input())
dq = deque(map(int, input().split()))
idx, cnt, res = 0, 0, ''

for i in range(n):
    if not dq:
        break
    elif len(dq) == 1 and idx < dq[0]:
        cnt += 1
        res += 'L'
        break
    
    l, r = dq[0], dq[len(dq) - 1]

    if  (l > r and idx > r and idx < l) or (l < r and idx < l):
        cnt += 1
        idx = dq.popleft()
        res += 'L'
    elif (l < r and idx > l and idx < r) or (l > r and idx < r):
        cnt += 1
        idx = dq.pop()
        res += 'R'
    else:
        break
print('%d\n%s' %(cnt, res))
