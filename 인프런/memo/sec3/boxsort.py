# 창고 정리

n = int(input())

box_cnt = list(map(int, input().split()))

m = int(input())

box_cnt.sort()

for _ in range(m):
    box_cnt[0] += 1
    box_cnt[-1] -= 1
    box_cnt.sort()

print(box_cnt[-1] - box_cnt[0])