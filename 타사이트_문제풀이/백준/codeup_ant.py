# 10 x 10

# (2, 2) 시작
list = [[1,1,1,1,1,1,1,1,1,1]
        ,[1,0,0,1,0,0,0,0,0,1]
        ,[1,0,0,1,1,1,0,0,0,1]
        ,[1,0,0,0,0,0,0,1,0,1]
        ,[1,0,0,0,0,0,0,1,0,1]
        ,[1,0,0,0,0,1,0,1,0,1]
        ,[1,0,0,0,0,1,2,1,0,1]
        ,[1,0,0,0,0,1,0,0,0,1]
        ,[1,0,0,0,0,0,0,0,0,1]
        ,[1,1,1,1,1,1,1,1,1,1]]
# 2 인가?
# 오른쪽이 0인가?
# 아래가 0인가?
# 멈춤

x = 1
y = 1

while True:
    dx = x
    dy = y
    if list[x][y] == 2:
        list[x][y] = 9
        break
    elif list[x][y + 1] == 2:
        list[x][y + 1] = 9
        break
    elif list[x + 1][y] == 2:
        list[x + 1][y] = 9
        break
    elif list[x][y + 1] == 0:
        y += 1
    elif list[x + 1][y] == 0:
        x += 1
    else :
        list[x][y] = 9
        break
    list[dx][dy] = 9

for i in list:
    print(i)
    print()