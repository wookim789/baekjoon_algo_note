# 이진 탐색을 지원해주는 라이브러리

from bisect import bisect_left, bisect_right

# 이진 탐색은 정렬된 iterator 객체에서만 사용가능

arr = [1, 2,3,7,98,2,6,5,4,7,23,9,5,10]

# 이진 탐색전 정렬 필수
arr.sort()

# 7의 위치를 찾아보자
print(arr)
print(bisect_left(arr, 7))
print(bisect_right(arr, 7))

# 결과를 보면 의아해 하는데 차이가 2가 나는이유는

# 6, 7, 7, 9 
# bisect_left는 6,7 에서 6의 인덱스를 리턴
# bisect_right는 7,9에서 9의 인덱스를 리턴

# 위 이진 탐색을 이용해서
# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구할떄 효과적

def count_by_range(a, l_val, r_val):
    l_idx = bisect_left(a, l_val)
    r_idx = bisect_right(a, r_val)

    return r_idx - l_idx
# 값이 4인 개수 출력
print(count_by_range(arr, 4, 4))

# 값이 1부터 5인 개수 출력
print(count_by_range(arr,1,7))