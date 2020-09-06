# 2개의 배열을 비교하며 정렬
# 2 pointer sort

n, m = 3, 4

a = [1, 3, 5]
b = [2, 4, 6, 8]

result = []


i, j = 0, 0

# 하나의 배열이라도 구간을 벗어나지 않았다면 반복
while i < n or j < m:
    # j는 구간을 벗어났다면 -> i도 벗어났다면 while문이 종료되므로 i는 구간 내에 있다
    # j와 i가 구간내에 있고, a[i]가 b[j] 보다 작거나 같다면
    if j >= m or (i < n and a[i] <= b[j]):
        result.append(a[i])
        i += 1    
    else:
        result.append(b[j])
        j += 1
print(result)
        

