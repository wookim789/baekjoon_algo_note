string = input()

idx = 1
for s in string:
    if idx == 11:
        idx = 1
        print()
    print(s, end = '')
    idx += 1