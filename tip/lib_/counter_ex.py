from collections import Counter

a = Counter([1, 1 ,1, 3, 4, 4 ,4])
b = Counter([1, 1, 3, 4])
# print(a)
# print(a - b)
# print(dict(a))
# print(dict(a-b))

for key, value in a.items():
    pass
    # print(key, value)





from collections import OrderedDict

d = {}
d["c"] = 1
d["a"] = 2
d["b"] = 1
# print(d)

for key, value in d.items():
    pass
    # print(key, value)

od = OrderedDict()
od["c"] = 1
od["a"] = 2
od["b"] = 1
# print(od)

for key, value in od.items():
    pass
    # print(key, value)





# 1 [cpp, java, python]
# 2 [backend, frontend]
# 3 [ junior, senior]
# 4 [chicken, pizza ]
lang_list = ["cpp", "java", "python"]
bf_list = ["backend", "frontend"]
js_arr = ["junior", "senior"]
pc_arr = ["pizza", "chicken"]

l_g = dict()
for lang in lang_list :
    b_f = dict()
    for bf in bf_list:
        j_s = dict()
        for js in js_arr:
            p_c = dict()
            for pc in pc_arr:
                p_c[pc] = []
            j_s[js] = p_c
        b_f[bf] = j_s
    l_g[lang] = b_f
print(l_g)


l_g[q_arr[0]][q_arr[1]][q_arr[2]][q_arr[3]]