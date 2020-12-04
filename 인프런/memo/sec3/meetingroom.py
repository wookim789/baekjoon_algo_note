# 회의실 배정

n = int(input())

# 튜플로 데이터 받기
sch = [tuple(map(int, input().split())) for _ in range(n)]

# 튜플 2번째 인자로 정렬하기 : 강의 노트를 
sch.sort(key = lambda x : x[1]) 

ed = 0
cnt = 0

for s, e in sch:
    if ed <= s:
        cnt += 1
        ed = e

print(cnt)




