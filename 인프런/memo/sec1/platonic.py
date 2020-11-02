n, m = map(int, input().split())

max_val = n + m

cnt_arr = [0] * (max_val + 1)

for ni in range(1, n + 1):
    for mi in range(1, m + 1):
        cnt_arr[ni + mi] += 1

result = []
max_num = max(cnt_arr)
for i in range(len(cnt_arr)):
    if cnt_arr[i] == max_num:
        result.append(i)

result.sort()
for i in result:
    print(i, end =' ')

