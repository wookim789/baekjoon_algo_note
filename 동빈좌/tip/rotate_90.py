def rotate_90(m):
    N = len(m)
    # 2차원 배열은 컴프리 헨션으로 선언해야 행마다 새 객체로 이루어짐
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret