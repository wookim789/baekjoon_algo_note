# 암호 만들기 
# 2
# 50분
# 1, 12mb

# 서로다른 L개의 알페벳 소문자
# 최소 한개의 모음
# 최소 2개의 자음
# 알파벳 -> 오름차순 정렬

# 3 <= l <= c <= 15
from itertools import combinations

c, l = map(int, input().split())

arr = list(map(str, input().split()))

result = combinations(arr, c)

moums =('a', 'e', 'i', 'o', 'u')
for i in result:
    moum_count = 0
    for moum in moums:
        moum_count += i.count(moum)
    if 0 < moum_count < c - 1:
        print(''.join(i))

# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw