# 배열을 순회하며 연속된 숫자의 합이
# 특정 값인 조합의 수를 구하는 문제
# 2 poninter 을 이용하여 구현한다

arr = [2, 3, 5, 3, 2, 3]

answer = int(input())

sums, ed, count = 0, 0, 0


for start in range(len(arr)):
    for end in range(ed, len(arr)):
        if start == end:
            sums = arr[end]
        elif start < end and end != ed:
            sums += arr[end]
        
        if sums < answer:
            continue
        elif sums == answer:
            count += 1
        elif sums > answer:
            sums -= arr[start]
            ed = end
            break

print(count)