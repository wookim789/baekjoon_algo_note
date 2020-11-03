# 1 <= N   (행)
# M <= 100 (열)

# 1 이상 10,000 이하의 자연수 int


if __name__ == "__main__":

############################################################################################################
# 1번 문제 풀이

# 행 비교 M
# 열 비교 N
# 최악은 NM

    n, m =  map(int, input().split())

    matrix = []

    inputData = input()
    while inputData != "end":
        matrix.append(list(map(int, inputData.split())))
        inputData = input()

    print(matrix)

    maxCardList = []

    for row in matrix:
        maxCardList.append(min(row))

    print(max(maxCardList))


############################################################################################################
# 2번 문제 풀이

# 정렬 NlongN
# 2MlogM * NlogN
# 2MNlog(M+N)

    n, m =  map(int, input().split())

    matrix = []

    inputData = input()
    while inputData != "end":
        matrix.append(list(map(int, inputData.split())))
        inputData = input()

    print(matrix)

    result = 0
    for row in matrix:
        row.sort()
        minIdx = row[0]
        if result < minIdx:
            result = minIdx

    print(result)