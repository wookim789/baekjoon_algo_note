# itertolls 순열과 조합의 기능을 제공하는 라이브러리

# 순열 라이브러리
from itertools import permutations

arr = ['a', 'b', 'c']

# 3개중 2개를 뽑아 나열하는 모든 경우의수 : 순열 nPr 
# nPr = n! / (n-r)!
result = list(permutations(arr, 2))
print(result)




# 조합 라이브러리
from itertools import combinations

arr = ['a', 'b', 'c']

# 3개중 2개를 순서에 상관없이 뽑는 경우의 수 : 조합 nCr
# nCr = n! /(n-r)!(r)!
result = list(combinations(arr, 2))
print(result)




# 중복 뽑기를 허용하는 순열 구하기
from itertools import product

arr = ['a', 'b', 'c']

result = list(product(arr, repeat=2))
print(result)




# 중복 뽑기를 허용하는 조합 구하기

from itertools import combinations_with_replacement

arr = ['a', 'b', 'c']
result = list(combinations_with_replacement(arr, 2))
print(result)