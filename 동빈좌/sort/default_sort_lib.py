arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 기본 정렬 
print(sorted(arr))
print(arr)

# 실제 배열이 정렬 되지는 않으니 할당을 해줘야함
arr = sorted(arr)
print(arr)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 아래가 더 효율적임
arr.sort()
print(arr)


# 튜블 정렬 예제
arr = [('바나나', 2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

arr = sorted(arr, key = setting)
print(arr)

arr = [('바나나', 2),('사과',5),('당근',3)]
arr = sorted(arr, key = lambda x:x[1])
print(arr)

