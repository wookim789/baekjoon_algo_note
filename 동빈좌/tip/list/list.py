# 파이썬의 list는 linked list 기반이다
# 따라서 append와 remove를 자원한다


a = [0, 1, 2, 3, 4]

# 엔덱싱과 슬라이싱
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])

print()
for i in a[2:-2]:
    print(i, end =' ')

print()
for i in a[2:-1]:
    print(i, end =' ')


# 리스트 컴프리헨션
print()
arr = [i for i in range(20) if i % 2 == 1]
print(arr)
print()

# 2차원 리스트 컴프리헨션
# 2차원 리스트는 반드시!!! 컴프리헨션으로 초기화 할것
# 2 x 3 행렬 초기화 
n = 2
m = 3
arr = [[0] * m for _ in range(n)]
print(arr)

# list 주요 메소드
idx, val = 0, ''
a.append()           #O(1)
a.sort()             #O(NlogN)
a.sort(reverse=True) #O(N)
a.insert(idx, val)   #O(N)
a.count('')          #O(N)
a.remove('')         #O(N)




# 부록

# linked 리스트와 
# array 리스트의 차이점

# linked : 원소 중간 추가 삭제가 매우 편리하고 빠르게 진행됨
# 대신 읽는 속도가 느림 -> 순차 탐색 O(N)

# arrayList : 원소 중간 추가 삭제가 매우 느림 : 기존 원소 재배열
# 또 새 원소를 추가할 때, 스택영역이 넘어서면
# 특정 수만큼 메모리를 할당해야함 -> 부하 발생
# 대신 읽는 속도가 매우 빠름 O(1)


