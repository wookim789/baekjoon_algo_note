n = int(input())

idx = 0
for i in range(2 * n):

    if i >= n:
        idx -= 1
    else:
        idx += 1
    print('*' * idx)
