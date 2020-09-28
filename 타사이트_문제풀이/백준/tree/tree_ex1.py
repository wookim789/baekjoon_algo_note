# 부모 트리 찾기

import sys

n = int(sys.stdin.readline())

edges = [[] for i in range(n + 1)]

for idx in range(1, n):
    f, s = map(int, sys.stdin.readline().split())
    edges[f].append(s)
    edges[s].append(f)

graph = [0] * (n + 1)

stack = []
stack.append([edges[1], 1, 1])
while stack:
    data = stack.pop()
    edge, root, cur = data[0], data[1], data[2]
    if root == 1 and root == cur:
        for i in edge:
            graph[i] = root
            stack.append([edges[i], root, i])
    else:
        for i in edge:
            if i != root:
                graph[i] = cur
                stack.append([edges[i], cur, i])

for i in range(2, n +1):
    print(graph[i])


# 입력
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7

# 출력 
# 4
# 6
# 1
# 3
# 1
# 4


# 12
# 1 2
# 1 3
# 2 4
# 3 5
# 3 6
# 4 7
# 4 8
# 5 9
# 5 10
# 6 11
# 6 12