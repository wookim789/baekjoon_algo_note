# 순차 탐색
# 배열의 처음부터 탐색하여 원하는 값과 일치하는 원소를 찾는 알고리즘
# 최악의 경우 O(n)

target = 'abc'

arr = ['a', 'b', 'c', 'abc']

def sequential_serach(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1
    return None

print(sequential_serach(arr, target))