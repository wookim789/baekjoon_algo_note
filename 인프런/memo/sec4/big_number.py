# 가장 큰 수

num, m = map(int, input().split())

# 맨앞에서 부터 이후 숫자가 이전 숫자보다 크다면 이전 숫자 제거
num = list(map(int, str(num)))
stack = []

for n in num:
    while stack and stack[-1] < n and m > 0:
        stack.pop()
        m -= 1
    stack.append(n)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)

