# 덩치

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank, end=' ')

# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

