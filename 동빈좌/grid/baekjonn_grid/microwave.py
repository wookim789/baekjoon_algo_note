# 1초 64MB 메모리 활용 문제


# a b c : 5분, 1분, 10초
# 300, 60, 10

# 입력 1 ≤ T ≤ 10,000

# 시간이 초단위라면 c버튼을 한번 더 둘러 야 한다.
# -> 올림 연산 

time = int(input())

time_list = [300, 60, 10]

result = []
for sec in time_list:
    divide = time//sec
    result.append(divide)
    time -= sec * (time//sec)

if time != 0:
    result = [-1]

for i in result:
    print(i, end=' ')