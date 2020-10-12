# 2초 128mb 
import heapq
import sys

n = int(input())

schedule = []
for i in range(n):
    st, ed = map(int, sys.stdin.readline().split())
    heapq.heappush(schedule, tuple([ed, st]))

st = 0
result = 0

while schedule:
    tmp = heapq.heappop(schedule)
    if st <= tmp[1]:
        result += 1
        st = tmp[0]

print(result)



