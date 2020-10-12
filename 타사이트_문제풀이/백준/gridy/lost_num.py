# 잃어버린 번호
# 2s 128mb

import sys
from collections import deque

equation = sys.stdin.readline().rstrip()
oper_que = deque()
number_que = deque()

idx = 0
st_idx = 0
for s in equation:
    if s == '+' or s == '-':
        tmp = int(equation[st_idx : idx])
        oper_que.append(s)
        number_que.append(tmp)
        st_idx = idx + 1 
    idx += 1

tmp = int(equation[st_idx:])
number_que.append(tmp)

result = number_que.popleft()
tmp = 0

is_minus = False
for _ in range(len(oper_que)):
    oper = oper_que.popleft()

    if not is_minus and oper == '+':
        result += number_que.popleft()
    else:
        tmp += number_que.popleft()
        is_minus = True
result -= tmp
print(result)