# 럭키 스트레이트
# 1
# 20
# 1 128

# N = ab de => a + b = d + e => lucky

n = int(input())
st = str(n)

half_idx = len(st)//2

idx = 0
count = 0
for i in st:
    if idx < half_idx:
        count += int(i)
    else:
        count -= int(i)
    idx += 1
if count == 0:
    print('LUCKY')
else:
    print('READY')

# 입력예
# 123321 luck
# 2244 raedy
# 124331 luck

# 8분 컷