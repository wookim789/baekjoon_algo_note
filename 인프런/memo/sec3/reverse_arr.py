
n = int(input())
arr = list(map(int, input().split()))
res = [n + 1] * n

# 자신의 인덱스 위치까지 오면서 작은수를 만나면 인덱스를 증가시킨다.

idx = 1
for i in arr:
    j = 0
    min_cnt = 0
    check = 0
    while True:
        if res[j] < idx:
            min_cnt += 1
            check += 1
        if j < i:
            j += 1
        elif check > 0:
            j += 1
            check -= 1
        else:
            break
        
    res[i + min_cnt] = idx
    idx += 1

for i in res:
    print(i, end =' ')
