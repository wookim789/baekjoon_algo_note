n = int(input())

tot = 0
idx = 0
for i in range(1, n+1):
    if tot < n:
        tot += i
        idx = i
    elif tot >= n:
        idx = i - 1
        tot -= idx
        break

z_idx = 0
o_idx = 0
if idx % 2 == 0:
    tmp = [1, idx]
    z_idx = 1
    o_idx = -1
else:
    tmp = [idx, 1]
    z_idx = -1
    o_idx = 1

while tot < n - 1:
    tot += 1
    tmp[0] += z_idx
    tmp[1] += o_idx

print(str(tmp[0])+'/'+str(tmp[1]))