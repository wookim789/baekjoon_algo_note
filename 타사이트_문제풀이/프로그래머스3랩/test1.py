def solution(routes):
    
    mi = 30000
    ma = -30000
    
    for i in routes:
        mi = min(mi, min(i))
        ma = max(ma, max(i))
    
    highway = {}
    for i in range(mi, ma):
        highway[i] = 0

    for i in routes:
        for idx in range(i[0], i[1] + 1):
            highway[idx] += 1
    key_list, val_list = list(highway.keys()), list(highway.values())

    result = 0
    while len(routes) > 0:
        for i in routes:
            # print(i)
            tmp = len(routes)
            routes[:] = [i for i in routes if not i[0] <= key_list[val_list.index(max(val_list))] <= i[1]]
            if tmp > len(routes):
                result += 1
        val_list[val_list.index(max(val_list))] = 0
    return result

solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])