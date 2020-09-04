# 음료수 얼려 먹기
# 30분 1초 129mb 

# N x M

# n = int(input)
# m = int(input)

# graph = list(map(int, input().split()))

from collections import deque

n, m = 4, 5
graph = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,1,1,1,1],
         [0,0,0,0,0]]


# 2차원 좌표로 주어져도 그래프 탐색은 가능하다

