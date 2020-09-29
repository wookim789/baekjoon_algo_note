# 더하기 사이클

answer = int(input())

cur = -1
cnt = 0

while True:
    if cur == answer:
        break
    if cur == -1:
        cur = answer
    if cur < 10:
        cur = 10 * cur + cur
    else:
        mod = divmod(cur, 10)
        cur = mod[1] * 10 + (mod[0] + mod[1]) % 10
    cnt += 1
print(cnt)