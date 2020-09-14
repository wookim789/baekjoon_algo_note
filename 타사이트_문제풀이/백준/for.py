# 포문 문제

##############################################################################################################
# 구구단
n = int(input())

for i in range(1, 10):
    print(f'{n} *', i, f'= {n * i}')


##############################################################################################################
# a + b 출력
n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append(a + b)

for i in data:
    print(i)


##############################################################################################################
# 1~n 합 구하기
n = int(input())

result = 0
for i in range(1, n + 1):
    result += i
print(result)


##############################################################################################################
# 빠른 a + b
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)


##############################################################################################################
# 1부터 n 출력
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    print(i)


##############################################################################################################
# n 부터 1 출력
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n, 0, -1):
    print(i)


##############################################################################################################
# a + b - 7
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{i}: {a + b}')

##############################################################################################################
# a + b - 8
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f'Case #{i}: {a} + {b} = {a + b}')


##############################################################################################################
# 별 찍기
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print('*', end = '')
    print()


##############################################################################################################
# 오른쪽 정렬 별찍기
n = int(input())

for i in range(1, n + 1):
    space_num = n - i
    for k in range(space_num):
        print(' ', end = '')
    for j in range(i):
        print('*', end = '')
    print()

##############################################################################################################
# x보다 작은 수
n, x = map(int, input().split())
data = list(filter(lambda y : y < x, map(int, input().split())))
for i in data:
    print(i, end = ' ')


