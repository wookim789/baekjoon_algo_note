# ox 문제

n = int(input())



for _ in range(n):

    prob = input().split('X')
    tot = 0
    cur = 1
    for o_list in prob:
        for o in o_list:
            tot += cur
            cur += 1
        cur = 1
    print(tot)
