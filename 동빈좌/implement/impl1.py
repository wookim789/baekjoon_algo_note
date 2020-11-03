if __name__ == "__main__":
    # N = int(input())

    # wayList = list(map(str, input().split()))

    # codi = [1, 1]

    # for i in range(0, len(wayList)):
    #     if wayList[i] == 'R':
    #         wayList[i] = [0, 1]
    #     elif wayList[i] == 'L':
    #         wayList[i] = [0, -1]
    #     elif wayList[i] == 'U':
    #         wayList[i] = [-1, 0]
    #     elif wayList[i] == 'D':
    #         wayList[i] = [1, 0]

    # for way in wayList:
    #     if codi[0] + way[0] > 1 and codi[0] + way[0] <= N:
    #         codi[0] += way[0]
    #     if codi[1] + way[1] > 1 and codi[1] + way[1] <= N:
    #         codi[1] += way[1]

    # print(codi)




#########################################################################################################

    # 이동 경로 문제에서 dx, dy의 배열 처럼 이동 경로를 리스트로 작성하는 방법은 자주 사용된다
    9
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    # L, R, U, D 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]  
    move_types = ['L', 'R', 'U', 'D']

    # 이동 계획을 하나씩 확인
    for plan in plans:
        # 이동 후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny

    print(x, y)