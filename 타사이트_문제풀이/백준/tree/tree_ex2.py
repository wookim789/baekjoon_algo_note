# 트리의 지름

import sys

n = int(sys.stdin.readline())

edges = [[]]
for i in range(n):
    edges.append(list(map(int, sys.stdin.readline().split())))
print(edges)
matrix = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix[i][i] = 0

for i in range(1, n + 1):
    edge = edges[i]
    mt_idx = edge[0] - 1

    for e_idx in range(1, len(edge), 2):
        if edge[e_idx] != -1:
            matrix[mt_idx][edge[e_idx]-1] = edge[e_idx + 1]
print(matrix)

# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1

recur_stack = []
root = 0
cur = 0
length = 0
recur_stack.append([root, cur, length])

while recur_stack:
    data = recur_stack.pop()
    root, cur, length = data[0], data[1], data[2]
    idx = 0
    for col in matrix[root]:
        if col != 0 and col != -1 :
            length += col
            recur_stack.append([root, idx, length])
        idx += 1

# [[ 0, -1,  2, -1, -1], 
#  [-1,  0, -1,  4, -1], 
#  [ 2, -1,  0,  3, -1], 
#  [-1,  4,  3,  0,  6], 
#  [-1, -1, -1,  6,  0]]