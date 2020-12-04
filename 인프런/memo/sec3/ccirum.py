# 씨름 

n = int(input())

info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key = lambda x : x[0], reverse=True)

largrest_weight = 0
cnt = 0

for h, w in info:
    if w > largrest_weight:
        largrest_weight = w
        cnt += 1

print(cnt)