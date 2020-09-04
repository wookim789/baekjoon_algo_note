# 1초 256MB
# 1 <= N <= 1000
# 1 <= p <= 1000

# 5
# 3 1 4 3 2

# 걸리는 시간 정렬
# 배열 하나에 자신 전의 모든 사람이 걸리는 시간 더하여 저장

tot = int(input())

people = list(map(int, input().split()))
people.sort()

integral = []

time_sum = 0

for time in people:
    time_sum += time
    integral.append(time_sum)

result = 0
for i in integral:
    result += i

print(result)