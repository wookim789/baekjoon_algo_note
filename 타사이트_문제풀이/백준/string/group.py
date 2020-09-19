# 그룹 단어

n = int(input())

arr = []
for i in range(n):
    arr.append(input())

result = 0
for s in arr:
    group = True
    s_set = set()
    tmp = ''
    for idx in s:
        count = len(s_set)
        if idx != tmp:
            s_set.add(idx)
            tmp = idx
            if count == len(s_set):
                group = False
                break
    if group:
        result += 1
print(result)

# 3
# happy
# new
# year