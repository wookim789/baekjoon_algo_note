# 팀 결성
# 2
# 풀이시간 20분
# 시간제한 2초
# 메모리 제한 128mb

# 0 ~ N 까지 총 N+1명
# 팀 합치기 연선 + 같은 팀 여부 확인

# 서로소 집합여부

n, m = map(int, input().split())


# 0 a b : a와 b 같은팀 합치기
# 1 a b : a와 b 같은 팀인지 확인
cal = [[0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]]
# for i in range(m):
#     cal.append(list(map(int, input().split())))

print(cal)


team = [i for i in range(n+1)]

print(team)

def make_team(a, b):
    global team
    a = check_team(team[a])
    b = check_team(team[b])

    if a > b:
        team[a] = b
    elif a < b:
        team[b] = a
        
def check_team(a):
    global team
    if team[a] != a:
        team[a] = check_team(team[a])
    return team[a]

def compare_team(a, b):
    global team

    a = check_team(a)
    b = check_team(b)

    if a == b:
        return 'YES'
    else:
        return 'NO'

for i in cal:
    if i[0] == 0:
        make_team(i[1], i[2])
    else:
        print(compare_team(i[1], i[2]))