# 씨름 

n = int(input())

info = [tuple(map(int, input().split())) for _ in range(n)]

info.sort(key = lambda x : x[0])
cnt = n


for f in range(n):
    for s in range(n):
        if f != s and info[f][0] < info[s][0] and info[f][1] < info[s][1]:
            cnt -= 1
            break
print(cnt)