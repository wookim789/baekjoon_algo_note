# 창고 정리

n = int(input())

box_cnt = list(map(int, input().split()))

m = int(input())


for _ in range(m):
    mx = max(box_cnt)
    mx_idx = box_cnt.index(mx)

    mi = min(box_cnt)
    mi_idx = box_cnt.index(mi)

    box_cnt[mx_idx] -= 1
    box_cnt[mi_idx] += 1

print(max(box_cnt) - min(box_cnt))