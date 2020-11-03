# 두 배열의 원소 교체
# 난이도 하
# 풀이시간 20분
# 시간제한2초, 메모리 128mb

# 1시 3분 까지

# n, k = map(int, input().split())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

n = 5
k = 3
a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]
a.sort()
b.sort(reverse=True)

for idx in range(k):
    if a[idx] < b[idx]:
        a[idx], b[idx] = b[idx], a[idx]
    else:
        break
print(sum(a))