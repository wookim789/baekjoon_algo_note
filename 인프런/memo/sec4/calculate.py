s = input()

res = ''
# 3+5*2/(7-2)
# 352*72-/+

# 3*(5+2)-9
# 352+*9-

stack = [] # 후 순위 연산
oper = ''  # 선 순위 연산
#  + - * / ( )

# 재귀 함수
def set_equation_recur(eq):
    res = ''
    row_oper = ''
    hig_oper = ''
    st = []
    i = 0
    # 문자열 연결
    while True:
        if i >= len(eq):
            res += hig_oper
            break
        if eq[i].isdigit():
            res += eq[i]
            res += hig_oper
            hig_oper = ''
        elif eq[i] == '+' or eq[i] == '-':
            row_oper += eq[i]
        elif eq[i] == '*' or eq[i] == '/':
            hig_oper = eq[i]
        else: # 재귀 호출
            recur = ''
            j = i
            while True:
                if eq[j] == '(':
                    st.append(eq[j])
                elif eq[j] == ')':
                    st.pop()
                
                if not len(st) > 0:
                    break
                recur += eq[j]
                j += 1
            recur = recur[1:]
            print(recur)
            res += set_equation_recur(recur)
            i = j
        i += 1
    res += row_oper
    return res

print(set_equation_recur(s))

    # 연산자 처리
    # 재귀 호출
