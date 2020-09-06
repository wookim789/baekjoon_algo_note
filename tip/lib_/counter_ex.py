from collections import Counter

a = Counter([1, 1 ,1, 3, 4, 4 ,4])
b = Counter([1, 1, 3, 4])
print(a)
print(a - b)
print(dict(a))
print(dict(a-b))

for key, value in a.items():
    print(key, value)






from collections import OrderedDict

d = {}
d["c"] = 1
d["a"] = 2
d["b"] = 1
print(d)

for key, value in d.items():
    print(key, value)

od = OrderedDict()
od["c"] = 1
od["a"] = 2
od["b"] = 1
print(od)

for key, value in od.items():
    print(key, value)