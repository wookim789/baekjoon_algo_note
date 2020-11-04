n = int(input())

dp_table = []

dp_table.append(1)
dp_table.append(2)

for i in range(2, n):
    next_eq = (dp_table[i - 1] + dp_table[i - 2]) % 10007
    dp_table.append(next_eq)

print(dp_table[n-1])