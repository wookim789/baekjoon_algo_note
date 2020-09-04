# 퀵 정렬 
# O(nlogn)
# 가장 널리 사용하는 알고리즘
# 거의 정렬된 경우 O(n^2)
# 거의 정렬된 경우 퀵이 아닌 삽입정렬을 사용한다
# 분할 정복 기법을 사용한다
# 가장 왼쪽으로 pivot을 정하고
# pivot을 제외한 가장 왼쪽과 가장 오른쪽을 서로 비교한다
# 왼쪽은 pivot보다 큰값을 찾고
# 오른쪽은 pivot보다 작은값을 찾는다
# 서로 인덱스가 엇갈리지 않았다면 swap
# 왼쪽은 오른쪽으로, 오른쪽은 왼쪽으로 인덱스 변경
# 계속 반복
# 만약 왼쪽 인덱스가 오른쪽 인덱스보다 커졌을 때
# 오른쪽 인덱스와(작은 녀석) 피봇값을 변경한다

# 피봇 기준으로 왼쪽, 오른쪽 각각 재귀함수 호출


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    # 재귀 종료 조건
    if start >= end : # 원소가 하나면 리턴
        return 

    pivot = start
    ldx = start + 1
    rdx = end

    while ldx <= rdx: 
        # 왼쪽 인덱스 찾기
        while ldx <= end and arr[pivot] >= arr[ldx]:
            ldx += 1
        # 오른쪽 인덱스 찾기
        while rdx > start and arr[pivot] <= arr[rdx] :
            rdx -= 1

        if ldx > rdx:
            arr[pivot], arr[rdx] = arr[rdx], arr[pivot]
        else:
            arr[ldx], arr[rdx] = arr[rdx], arr[ldx]

    
    # 왼쪽 재귀
    quick_sort(arr, start, rdx - 1)
    # 오른쪽 재귀
    quick_sort(arr, rdx + 1, end)

quick_sort(arr, 0, len(arr) - 1)
print(arr)