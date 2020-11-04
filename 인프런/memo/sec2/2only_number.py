# 숫자만 추출

s = input()

result = 0

for c in s:
    if c.isdigit():
        result = result * 10 + int(c)

h = result // 2

cnt = 0
for i in range(1, h + 1):
    if result % i == 0:
        cnt += 1

print(result)
print(cnt + 1)