s = 'abcabcabcabcdededededede'

answer = []


st = s[0]
count = 0
result = ''
n = 1    
# 1일때
for n in range(1,len(s)-1):
    st = s[0:n]
    for i in range(0,len(s),n):
        if st == s[i:i+n]:
            count += 1
        else:
            if count > 1:
                result += str(count) + st
            else:
                result += st
            st = s[i:i+n]
            count = 1
    if count > 1:
        result += str(count) + st
    else:
        result += st
    answer.append(len(result))
    result = ''
    count = 0

print(min(answer))