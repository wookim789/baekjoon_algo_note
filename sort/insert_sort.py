# 삽입 정렬
# 맨앞의 수는 정렬되어 있다고 과정하고 시작
# 그 다음수가 맨앞의 수와 비교하여 더 작다면 swap

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break
print(arr)
