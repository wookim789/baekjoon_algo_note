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


# 위 로직을 필터를 이용하면 한줄로 가능
print(''.join(sorted((list(filter(lambda x : 65 <= ord(x) <= 90, st))))) + str(count))