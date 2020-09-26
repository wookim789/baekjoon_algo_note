# 피보나치 

# n = int(input())

# a = [0,1]

# for i in range(2,n+1):
#     a.append(a[i-1] + a[i-2])
# print(a[n])


case = int(input())
arr = []

for i in range(case):
    arr.append(int(input()))
pvio_arr =[[1,0],[0,1]]

def pivo(n):
    global pvio_arr
    for i in range(2, n+1):
        temp = list(zip(pvio_arr[i-1], pvio_arr[i-2]))
        pvio_arr.append([sum(temp[0]), sum(temp[1])])

pivo(max(arr))
for i in arr:
    print(pvio_arr[i][0], pvio_arr[i][1])