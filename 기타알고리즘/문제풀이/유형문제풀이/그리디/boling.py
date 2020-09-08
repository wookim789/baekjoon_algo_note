# 볼링공 고르기

# 1
# 30
# 1 128

# n개의 볼링공중 2개의 조합을 구함
# 2개의 볼링공의 무게가 다를 떄 count 1

from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
idx = [i for i in range(1, n+1)]
two_list = list(combinations(idx, 2))

result = len(two_list)
for i in two_list:
    if arr[i[0]-1] == arr[i[1]-1]:
        result -= 1
print(result)


# 12분 30초

# 입력 예
# 5 3
# 1 3 2 3 2

# 8 5 
# 1 5 4 3 2 4 5 2