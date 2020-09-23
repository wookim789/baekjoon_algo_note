# 체스판 칠하기

y, x = map(int, input().split())

m = []

for r in range(y):
    m.append(list(input()))


# 모든 8 x 8 영역을 순회한다


# 해당 영역에 바꿔야 하는 칸의 수를 센다
cnt = 0
for r in range(0, y - 7):
    for c in range(0, x - 7):
