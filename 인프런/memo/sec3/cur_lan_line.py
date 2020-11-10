# 랜선 자르기

n, m = map(int, input().split())

arr = [ int(input()) for _ in range(n)]

arr.sort()
print(arr)


st, ed = 0, max(arr)
mid_val = ed // 2
cnt = 0

while cnt != m :

    cnt = 0
    for i in arr:
        cnt += i // mid_val

    if cnt < m: # mid val 감
        ed = mid_val - 1
        mid_val = (st + ed) // 2
    elif cnt > m: # mid val 증
        st = mid_val + 1
        mid_val = (st + ed) // 2
print(mid_val)