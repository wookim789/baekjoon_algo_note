#다이얼
# UNUCIC : 36
s = input()

st_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO','PQRS','TUV','WXYZ']
time_list = [3, 4, 5, 6, 7, 8, 9, 10]
result = 0

for i in range(len(s)):
    for j in range(len(st_list)):
        if s[i] in st_list[j]:
            result += time_list[j]
            break
print(result)



