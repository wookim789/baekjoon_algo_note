# 스도쿠 정답 맞는지 확인하기

sduco = [ list(map(int, input().split())) for _ in range(9)]

def check(sduco):
    # 행, 열 검사
    for i in range(9):
        row_line = set()
        col_line = set()
        for j in range(9):
            if sduco[i][j] in row_line or sduco[j][i] in col_line:
                print('NO')
                return
            else:
                row_line.add(sduco[i][j])
                col_line.add(sduco[j][i])
    row_line = None
    col_line = None

    # 블록 검사
    for ridx in range(3):
        for cidx in range(3):
            line = set()
            for r in range(3):
                tmp = sduco[ridx * 3 : ridx * 3 + 3][r]
                for j in tmp[cidx * 3 : cidx * 3 + 3]:
                    if j in line:
                        print('NO')
                        return 
                    else:
                        line.add(j)
    print('YES')
check(sduco)