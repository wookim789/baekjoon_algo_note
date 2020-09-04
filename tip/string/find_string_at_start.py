
a = 'abc1234125123123'
c = '1abc123124124'
b = 'abc'
d = '24'


# 문자열에서 특정 문자 찾기
if b in a:
    print(True)
else:
    print(False)

if a.find(b) != -1:
    # 문자열에서 특정 문자 반결시 해당 글자의 첫 idx 리턴
    print(a.find(b))
else:
    # 없으면 -1 리턴
    print(False)

print()
# 문자열의 맨앞에 인자 문자열이 있는지 true/false 리턴
print(a.startswith(b))
print(c.startswith(b))

print()

# 문자열의 맨뒤에 인자 문자열이 있는지 true/false 리턴
print(a.endswith(d))
print(c.endswith(d))