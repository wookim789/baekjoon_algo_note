# 이진 탐색
# 이진탐색은 배열이 정렬되어 있을때만 사용 가능하다
# 정렬된 배열 탐색 시 원소를 빠르게 찾을수 있다

# 특징
# 탐색 범위를 절반씩 좁혀가며 데이터를 탐색한다

# 이진탐색은 위치를 나타내는 변수 3개를 사용한다
# 탐색하고자 하는 범위의 '시작점', '끝점' 그리고 '중간점'이다

### 찾으려는 데이터와 중간점 데이터와 반복적으로 비교해서 값 찾기

#### 탐색 범위가 2000만을 넘어가면 이진 탐색으로 문제에 접근해보자!


start = 0
end = 9

# target과 중간 지점과 비교
# 타겟이 더 작다면 시작점 ~ 끝점(중간지점) 설정해서 다시 탐색
# 타겟이 더 크다면 시작점(중간지점) ~ 끝점 설정해서 다시 탐색
# 타겟이 중간지점과 같다면 return

# 재귀함수로 작성 가능

target = 8
arr = [x for x in range(1,20,2)]
print(arr)

def search_bianry_recur(arr, st, end, traget):
    if st > end:
        return st
    mid = (st + end)//2
    result = 0
    if target == arr[mid]:
        result = mid
    elif target < arr[mid]:
        result = search_bianry_recur(arr, st, mid - 1, target)
    else:
        result = search_bianry_recur(arr, mid + 1, end, target)
    return result

print(search_bianry_recur(arr, 0, len(arr), target))