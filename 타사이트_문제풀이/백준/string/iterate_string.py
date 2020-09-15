# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:

n = int(input())

for i in range(n):
    r, s = input().split()
    r = int(r)

    for j in s:
        p = j * r
        print(p, end = '')
    print()