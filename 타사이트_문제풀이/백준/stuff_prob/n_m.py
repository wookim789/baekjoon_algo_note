from itertools import permutations, combinations

n, m = map(int, input().split())

p = permutations(range(1,n+1),m)

# for i in p:
    # pass
    # print(' '.join(map(str, i))) 


from itertools import permutations, combinations

n, m = map(int, input().split())
c = combinations(range(1,n+1),m)

for i in c:
    print(' '.join(map(str, i)))



