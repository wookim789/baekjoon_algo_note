# 배열을 순회하며 연속된 숫자의 합이
# 특정 값인 조합의 수를 구하는 문제
# 2 poninter 을 이용하여 구현한다
data = [1, 2, 3, 2, 5]

# answer = int(input())
n, m = 5, 5

sums, ed, count = 0, 0, 0


for start in range(len(data)):
    for end in range(ed, len(data)):
        if start == end:
            sums = data[end]
        elif start < end and end != ed:
            sums += data[end]
        
        if sums < m:
            continue
        elif sums == m:
            count += 1
        elif sums > m:
            sums -= data[start]
            ed = end
            break

print(count)



n = 5
m = 5

count, interval_sum, end = 0, 0, 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(count)