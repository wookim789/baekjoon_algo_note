n = int(input())
narr = list(map(int, input().split()))

m = int(input())
marr = list(map(int, input().split()))

nidx, midx = 0, 0
result = []
while True:
    if nidx == n and midx < m:
        result += marr[midx:]
        break
    elif nidx < n and midx == m:
        result += narr[nidx:]
        break
    
    if narr[nidx] > marr[midx]:
        result.append(marr[midx])
        midx += 1
    elif narr[nidx] <= marr[midx]:
        result.append(narr[nidx])
        nidx += 1

for i in result:
    print(i, end = ' ')
