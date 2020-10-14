# 호텔 방 배정

tc_num = int(input())

tc_list = []

for _ in range(tc_num):
    tc_list.append(list(map(int, input().split())))

for tc in tc_list:
    w, h = divmod(tc[2], tc[0])
    if h != 0:
        w += 1
    else:
        h = tc[0]
    
    if w < 10:
        w = '0' + str(w)
    
    print(str(h) + str(w))
