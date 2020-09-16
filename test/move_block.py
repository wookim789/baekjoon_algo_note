# 블록 이동

# 가로로 이동할떈 가로로
# 세로로 이동할땐 세로로
from collections import deque

def solution(board):
    answer = 0
    return answer



def rotate(codi):
    is_lay = codi[0][0]- codi[1][0]

    std = []
    
    if is_lay == 0: # 가로 방향이라면
        std.append(codi[1][0] + 1)
        std.append(codi[1][1])
    else:
        std.append(codi[1][0])
        std.append(codi[1][1] + 1)
    codi.popleft()
    codi.append(tuple(std))
    print(codi)
    return codi

codi = deque()
codi.append((1,1))
codi.append((2,1))

rotate(codi)

