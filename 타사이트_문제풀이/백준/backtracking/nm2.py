
# n과 m


def select(st, m, n):
    global result
    if m < 0:
        return
    for idx in range(st, n):
        if len(result) == 0 or result[-1] <= idx:
            result.append(idx)
        if m == 0:
            tmp = [str(i) for i in result]
            print(' '.join(tmp))
            result.pop()
        else:
            select(idx, m-1, n)
            result.pop()

n, m = map(int, input().split())
result = []
select(1, m-1, n+1)