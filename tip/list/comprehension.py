list_comprehension = [ x for x in range(10)]
print(list_comprehension)

list_comprehension = [ [x,y] for x in range(10) for y in range(2)]
print(list_comprehension)

list_comprehension = [ x for x in range(10) if x % 2 == 0]
print(list_comprehension)

list_comprehension = [ x for x in range(10) if x % 2 == 0 if x % 3 == 0]
print(list_comprehension)

list_comprehension = [[] for _ in range(3)]
print(list_comprehension)


