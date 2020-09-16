# 상수

# 문자열 거꾸로 비교

f, s = input().split()


print(max(f[::-1],s[::-1]))


# 방법 2

f, s = input().split()

l = list(f)
l.reverse()

print(''.join(l))