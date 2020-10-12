
self_list = dict()

for i in range(1, 10001):
    self_num = i
    el = str(i)
    for num in el:
        self_num += int(num)
    self_list[self_num] = i

for i in range(1, 10001):
    if i not in self_list.keys():
        print(i)
