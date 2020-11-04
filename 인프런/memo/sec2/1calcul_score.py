# n = int(input())

# for i in range(n):
#     s = input()
#     s = s.lower()
#     r = list(map(str, s))
#     r.reverse()
#     if s == ''.join(r):
#         print('#%d YES' %(i + 1))
#     else:
#         print('#%d NO' %(i + 1))

######################################

# n = int(input())

# for i in range(n):
#     s = input()
#     s = s.lower()
#     if s == s[::-1]:
#         print('#%d YES' %(i + 1))
#     else:
#         print('#%d NO' %(i + 1))


n = int(input())

for i in range(n):
    s = input()
    s = s.lower()
    for j in range(len(s) // 2):
        if s[j] != s[-1 - j]:
            print('#%d NO' %(i))
            break
    else:
        print('#%d YES' %(i))