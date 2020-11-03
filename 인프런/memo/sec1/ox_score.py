# ox점수 계산 문제

n = int(input())

arr = list(map(int, input().split()))

tot = 0
scr = 0
for i in arr:
    if i == 1:
        scr += 1
        tot += scr
    else:
        scr = 0
print(tot)