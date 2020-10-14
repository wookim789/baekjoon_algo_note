import sys

limit = 100

arr = []
for i in range(limit):
    arr.append(sys.stdin.readline().rstrip())

for i in arr:
    print(i)
