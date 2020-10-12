

arr = [0]
idx = 0
for i in range(9):
    data = int(input())
    tmp = arr.pop()
    if tmp < data:
        idx = i
        arr.append(data)
    else:
        arr.append(tmp)

print(arr.pop())
print(idx + 1)