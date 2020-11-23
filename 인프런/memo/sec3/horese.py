# 마구간

n, c = map(int, input().split())
point = [int(input()) for _ in range(n)]

# 정렬
point.sort()


# 최소값과 최대값에 말 배치
# 홀수개 -> 중간 배치 및 좌우 대칭
# 짝수개 -> 중간 배치 x 좌우 대칭
