# 트리의 지름

import sys
sys.setrecursionlimit(200000)

n = int(sys.stdin.readline())

edges = [[] for _ in range(n + 1)]
tot = []
idx_set = set()

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    idx = tmp[0]
    idx_set.add(idx)
    e_idx = 1
    while tmp[e_idx] != -1:
        edges[idx].append(tuple(tmp[e_idx : e_idx + 2]))
        e_idx += 2

def sum_cost_recur(w_list, cost, n_cost, c_idx):
    global edges, tot

    if c_idx in w_list:
        if (tot and max(tot) < cost - n_cost) or not tot:
            tot.append(cost - n_cost)
        return

    w_list.append(c_idx)

    for n_idx, n_cost in edges[c_idx]:
        sum_cost_recur(w_list, cost + n_cost, n_cost, n_idx)

for idx in idx_set:
        sum_cost_recur([], 0, 0, idx)
    
print(max(tot))
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1

