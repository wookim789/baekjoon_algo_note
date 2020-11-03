# 만들수 없는 금액
# 1
# 30
# 1 128

# n개의 동전
# n개으 ㅣ동전을 이용해서 만들 수 없는 양의 정수 금액중 최솟값 구하기

from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

# 만들수있는 동전의 합의 리스트

arr.sort()
combi = set(arr)
if arr[0] > 1:
    print(1)
else:
    for i in range(2, len(arr)):
        temp = list(combinations(arr, i))
        for j in temp:
            combi.add(sum(j))

result = list(combi)
result.sort()
print(result)
printed = False
for i in range(len(result)-1):
    if result[i+1] - result[i] > 1 and not printed:
        print(result[i] + 1)
        printed = True
if not printed:
    print(result[-1] + 1)

# 29qns 41초
# 32분 수정