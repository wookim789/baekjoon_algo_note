# 선택 정렬
# 배열의 가장 작은 수를 골라 맨앞으로 이동
# 시간복잡도 O(N^2) 으로 비효율적이다
# 다만 코딩테스트 문제에서 가장 작은 수를 찾는 기법이 자주 사용되니 익숙해질것

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)): # 가장 작은 수 선택 
    min_idx = i
    for j in range(i + 1, len(arr)): # 가장 작은 수를 찾기
        if arr[min_idx] > arr[j]: # 현재 원소가 더 작다면 sawp
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
