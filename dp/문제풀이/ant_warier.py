# 개미전사
# 난이도 2
# 풀이시간 30
# 1초, 128mb

# 56분까지

# max를 이용
# dp 문제

m = 7
arr = [1,2,1,4,5,7,3]
# m = 4
# arr = [1,3,1,5]

d = [0] * 100

d[0] = arr[0]

d[1] = max(arr[0],arr[1])

for x in range(2, m):
    d[x] = max(d[x-1], d[x-2] + arr[x] )
print(d[m-1])