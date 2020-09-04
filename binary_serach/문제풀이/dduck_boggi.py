# 떡볶이 떡 만들기
# 난이도 중
# 풀이시간 40분
# 2초, 128mb
# 4시 40분 까지

# 가장 긴 떡을 찾아야함
# 역순 정렬

# 가장 긴 떡의 길이로 설정하면 0
# 이후로 1cm 줄이면 가장 긴떡에서 1cm
# 2번째 긴떡의 높이까지 잘랐다면
# 가장긴떡 길이 - 2번째 떡 길이 
# 이후 3번째 긴 떡까지 잘랐다면 떡길이
# 가장 긴떡길이 - 3번째 떡길이
# 2번째 긴떡길이 - 3번째 떡길이

# n, m = map(int, input().split())

# arr = list(map(int, input().split()))

# n = 4
# m = 11
# arr = [19, 15, 10, 17]


# # 떡 길이 역순 정렬
# arr.sort(reverse=True)
# print(arr)
# heigt = arr[0]

# count = 0

# # 순차 탐색 -> 시간 초과
# def count(arr, m):
#     count = 0
#     for i in range(arr[0], 0, -1):
#         for d in arr:
#             if d > i and count < m:
#                 count += (d - i)
#                 if count >= m:
#                     return count
#             else:
#                 break
#         count = 0
# print(count(arr,m))


#####################################################

n = 4
m = 6
arr = [19, 15, 10, 17]

st = 0
end = max(arr)

result = 0
while st <= end:
    count = 0
    mid = (st + end)//2
    for i in arr:
        if i > mid:
            count += (i - mid)
    if count < m:
        end = mid - 1
    else:
        result = mid
        st = mid + 1
print(result)