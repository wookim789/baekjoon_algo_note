# 가장 많은 문자

from collections import Counter
s = dict(Counter(input().upper()))

values = list(s.values())
values.sort(reverse = True)

if len(values) > 1 and values[0] == values[1]:
    print('?')
else:
    i = 0
    result = ''
    for k in s.keys():
        if s[k] > i:
            result = k
            i = s[k]
    print(result)

