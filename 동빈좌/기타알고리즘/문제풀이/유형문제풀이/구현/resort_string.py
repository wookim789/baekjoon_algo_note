# 문자열 재정렬
# 1
# 20
# 1 128

# 알파벳 대문자와 숫자 0~9 숫자 문자열 입력

st = 'K1KA5CB7'

print(ord('A'))
print(ord('Z'))
print()
print(ord('0'))
print(ord('9'))
print()

count = 0
result = ''
for i in st:
    if 48 <= ord(i) <= 57:
        count += int(i)
    else:
        result += i


result = ''.join(sorted(result))
print(result + str(count))


print(''.join(sorted((list(filter(lambda x : 65<= ord(x) <=90, st))))) + str(count))

# 12분 컷