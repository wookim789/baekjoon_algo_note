# python 에서 map이든 set이든 hasKey() 함수 대신 in 을 사용해야 한다

data_set = set([1,2,3,3,4,5,5,5])
print(data_set)

a_set = set([1,2,3])
b_set = set([3,4,5])

# 교집합
# print(a_set.intersection(b_set))
print(a_set & b_set)

# 합집합
# print(a_set.union(b_set))
print(a_set | b_set)

# 차집합
# print(a_set.difference(b_set))
print(a_set - b_set)

# 값추가 o(1)
a_set.add(4)
print(a_set)

# 여러개 값 추가
a_set.update([1,2,3,4,5,5,6,7,7,8,9])
print(a_set)

# 특정값제거 o(1)
a_set.remove(1)
print(a_set)