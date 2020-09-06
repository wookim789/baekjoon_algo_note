# 구간합 계산

# 연속적으로 나열된 n개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제

# n : 배열 수
# st : 구간의 시작
# end : 구간의 끝

arr = [1,3,4,5,6,2,4,5,6,2,7,8,7,9,9,1,3,2,6,5,4,4,5]

st, end = map(int, input().split())
n = len(arr)

arr_sum = [0]


sum_tot = 0
for i in range(0, n):
    sum_tot += arr[i]
    arr_sum.append(sum_tot)


print(arr_sum)
print(f'{arr_sum[end]} - ', f'{arr_sum[st-1]} = ', arr_sum[end] - arr_sum[st-1])