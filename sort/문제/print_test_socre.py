# 성적이 낮은 순서로 학생 출력하기
# 20분, 난이도 하
# 1초, 128mb

n = int(input())

arr = []

while n > 0:
    data = tuple(input().split())
    arr.append(data)
    n -= 1
print(arr)


# def setting(arr):
#     return arr[1]

# arr.sort(key=setting)

arr.sort(key = lambda x : x[1])
print(arr)