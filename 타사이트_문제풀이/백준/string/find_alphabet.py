# 알파벳 찾기

alpha = [-1] * 26

st = input()

idx = 0
for s in st:
    if alpha[ord(s)-97] == -1:
        alpha[ord(s)-97] = idx
    idx += 1
for i in alpha:
    print(i, end=' ')

# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1