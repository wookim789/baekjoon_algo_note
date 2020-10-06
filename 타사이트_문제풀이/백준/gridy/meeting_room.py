# 회의실배정

# 그리디 문제
# 시작 시간이 가장 이른 스케줄 목록
# 종료 시간이 가장 짧은 스케줄 선택

# 다름 스케줄 중 종료 시간과 같거나 큰 스케줄 목록
# 종료시간이 가장 짧은 스케줄 선택


# 시작 가능 시간이 가장 작고, 종료시간도 가장 짧은 것만 고르면

# 리스트 중 첫번째 원소 선택
# 다음 원소와 시작시간 비교 + 종료 시간 비교
# 시작시간, 종료시간 모두 작다면 변경

import sys
import heapq

n = int(sys.stdin.readline())

schedule = []

for i in range(n):
    heapq.heappush(schedule, tuple(map(int, sys.stdin.readline().split())))

result = []
    
tmp_f = heapq.heappop(schedule)
st = tmp_f[0]
ed = tmp_f[1]
result.append(tmp_f)
while schedule:
    tmp = heapq.heappop(schedule)
    if tmp[0] == st and tmp[1] != tmp[0]:
        continue
    elif tmp[0] == st and tmp[0] == tmp[1]:
        st = tmp[0]
        ed = tmp[1]
        result.append(tmp)
    elif st < tmp[0] and tmp[1] < ed:
        st = tmp[0]
        ed = tmp[1]
        result.pop()
        result.append(tmp)
    elif ed <= tmp[0]:
        st = tmp[0]
        ed = tmp[1]
        result.append(tmp)
print(len(result))

print(result)
# 1 4
# 3 5
# 0 6
# 1 1
# 3 3
# 5 7
# 3 8
# 5 9
# 7 8
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

# 1 2
# 1 3
# 2 2
# 2 2
# 3 3
# 3 3
# 3 3
# 3 3


# 1 2
# 2 3
# 3 4
# 3 8
# 4 9
# 8 8
# 8 8
# 8 13
# 9 10
# 10 11
# 11 12