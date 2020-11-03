# 계수 정렬
# 정렬할 배열에 여러가지 조건이 만족할 때 사용 가능
# 1. 가장 작은 수와 가장 큰수간의 작은 편차
# 2. 양의 정수들로만 이루어진 배열
# 3. 크기가 한정되고, 중복이 많이 되어 있다면 계수정렬을 사용해도 좋다
# 시간복잡도 O(n + k)
# 공간복잡도 O(n + k)

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1


for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')