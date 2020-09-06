from math import sqrt

# 에라토스테네스의 체
# N을 입력받으면 2부터 N까지 모든 소수를 출력
# O(Nlog(logN)) : 빠르다

def eratosthenes(n):
    array = [True for i in range(n + 1)]
    for i in range(2, int(sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
                
    for i in range(2,len(array)):
        if array[i]:
            print(i, end=' ')



n = int(input())
eratosthenes(n)
