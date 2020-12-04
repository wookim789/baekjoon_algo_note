# 타이타닉
from collections import deque

n, max_w = map(int, input().split())
tmp_arr = list(map(int, input().split()))
tmp_arr.sort()

w_arr = deque()
for i in tmp_arr:
    w_arr.append(i)

cnt = 0
for i in range(n):
    if not w_arr:
        break
    mx = w_arr.pop()
    if not w_arr:
        cnt += 1
        break
    mi = w_arr.popleft()

    if mx + mi > max_w:
        w_arr.appendleft(mi)
    cnt += 1

print(cnt)


from collections import deque

dq = deque()
dq.append(1)
dq.appendleft(1)
dq.pop()
dq.popleft()