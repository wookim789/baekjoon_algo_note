# 부품 찾기
# 난이도 1.5 
# 풀이시간 30분
# 시간제한 1초, 메모리 128mb

# 중복없는 N개의 수

# 1 <= n <= 1000000
# 1 <= m <= 1000000

import sys

# n = int(input())
# n_arr = sys.stdin.readline().rstrip()

# m = int(input())
# m_arr = sys.stdin.readline().rstrip()

n = 5
n_arr = [8, 3, 7, 9, 2]

m = 3
m_arr = [7, 5, 9]

# 입력되는 데이터 사이즈가 굉장히 크다
# 문제는 데이터를 탐색하는 문제
# 이진 트리 탐색을 푸는것이 맞다고 생각된다


n_arr.sort()

answer = []

#  이진 탐색 재귀 함수
def bianry_serach_recur(arr, st, end, target):
    global answer

    # 재귀 함수 탈출 조건 명시
    if st == end and target == arr[st]:
        return 'yes'
    elif st == end and target != arr[st]:
        return 'no'

    mid = (st + end) // 2

    if target == arr[mid]:
        return 'yes'
    elif target > arr[mid]:
        return bianry_serach_recur(arr, mid + 1, end, target)
    else:
        return bianry_serach_recur(arr, st, mid - 1, target)
    

for k in m_arr:
    answer.append(bianry_serach_recur(n_arr, 0, n, k))

print(answer)






################################################################################
# 계수 정렬 
n = 5
n_arr = [8, 3, 7, 9, 2]

m = 3
m_arr = [7, 5, 9]

arr = [0] * 1000001

for i in n_arr:
    arr[i - 1] += 1

answer = []
for j in m_arr:
    if arr[j - 1] != 0:
        answer.append('yes')
    else:
        answer.append('no')
print(answer)


##################################################################################
# set
# 단순히 값이 있는지 없는지 확인하는 거라면
# set을 사용하면 hashSet이기에 빠르게 찾을 수 있다

n = 5
n_arr = set([8, 3, 7, 9, 2])

m = 3
m_arr = [7, 5, 9]

answer = []
for m in m_arr:
    if m in n_arr:
        answer.append('yes')
    else:
        answer.append('no')
print(answer)