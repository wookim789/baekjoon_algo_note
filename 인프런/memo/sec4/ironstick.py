data = input()


st, cnt, memo = 0, 0, '('
sta =[]
cnta = []
idxa = []
for idx in data:
    if idx == memo and idx == '(':
        st += 1
    elif idx == memo and idx == ')':
        st -= 1
        cnt += 1
    elif idx != memo and idx == '(':
        st += 1
    elif idx != memo and idx == ')':
        st -= 1
        cnt += st
    memo = idx
print(cnt)
