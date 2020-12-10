s = input()

res = ''
# 3+5*2/(7-2)
# 352*72-/+

# 3*(5+2)-9
# 352+*9-

stack = [] # 후 순위 연산
oper = ''  # 선 순위 연산
#  + - * / ( )

print(res)


# 재귀 함수
def set_equation_recur(eq):
    low_op = ''
    hig_op = ''
    stack = ''

    open = 0
    for i in range(len(eq)):
        s = eq[i]
        if s.isdigit() and not hig_op:
            stack += s
        elif s.isdigit() and hig_op:
            stack += s
            stack += hig_op
            hig_op = ''
        elif s == '+' or s == '-':
            low_op += s
        elif s == '*' or s == '/':
            hig_op = s
        else: # 재귀 호출
            

