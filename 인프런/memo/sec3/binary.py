n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

st, ed = 0, n - 1
while st <= ed:
    midx = (ed + st) // 2
    if arr[midx] == m:
        break
    elif arr[midx] > m:
        ed = midx - 1
    elif arr[midx] < m:
        st = midx + 1
        
print(midx + 1)



