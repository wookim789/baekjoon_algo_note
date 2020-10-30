# 조합 라이브러리
# from itertools import combinations

# n, k = map(int, input().split())

# arr = sorted(list(map(int, input().split())))

# combi = list(combinations(arr, 3))
# result = set()

# for c in combi:
#     result.add(sum(c))

# result = sorted(list(result), reverse = True)
# print(result[k-1])


# 배열에서 3가지를 순서에 상관없이 뽑는 방법의 수

n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

res = set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(arr[i] + arr[j] + arr[m])

res = sorted(list(res), reverse = True)
print(res[k-1])
