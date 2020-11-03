# list에서 remove함수는 O(N)이 걸린다
# 또 중복되는 원소 중 하나만 삭제된다
# insert()와 remove()를 남발하면 시간초가다

# 이중 set를 이용해 remove_all()를 구현하는 방법이다

arr = [0, 1, 2, 3, 4, 4, 4, 5, 6]

# 4와 5를 전부 지우고 싶을 때

r_set = set([4,5])
print('r_set:', r_set)

d_arr = [i for i in arr if i not in r_set]
print(d_arr)
