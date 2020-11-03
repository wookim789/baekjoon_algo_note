# 문자열 뒤집기
# 1
# 20분
# 2 128

# 문제의 해답을 정확히 파악할것
# 문제의 요구사항을 파악할것
# 제한조건을 파악할것


# 0 or 1로만 이루어진 문자열
# 문자열에 있는 모든 숫자를 전부 같게 만들려고함
# 연속된 같은 숫자를 뒤집을 수 있음
# 위 행동으로 모든 숫자가 전부 같게되는 최소 연산수를 구하는 문제

# 배열을 연속된 수들로 나눈다
# 0000 11 00
# 11 00 1111 000 1

# 0과 1의 집합의 수 중 더 적은 수의 집합을 뒤집는다

# 0000 '00' 00 -> 1
# 11 '11' 1111 '111' 1 -> 2

# 사실상 0과 1로 이루어진 집합의 수를 세면 답이 나온다


st = input()

zeros = []
ones = []

cur = st[0]
idx = 0
lenght = 0
for i in range(len(st)):
    if cur == st[i]:
        continue
    elif cur == '0':
        cur = '1'
        zeros.append(st[idx:i])
        idx = i
        lenght += len(zeros[-1])
    elif cur == '1':
        cur = '0'
        ones.append(st[idx:i])
        idx = i
        lenght += len(ones[-1])
if lenght < len(st):
    if cur == '0':
        zeros.append(st[-1])
    else :
        ones.append(st[-1])

print(min(len(zeros), len(ones)))

# 32분컷... 12분초과
# 예상치 못한 for문 오류
