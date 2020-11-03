# 거스름돈

# 1초 125MB    big-0 : nlogn

# 큰 동전부터 개수를 채우며 진행

# 동전 개수 리턴

# ex) 380 : 4
pay = int(input())

tot = 1000 - pay
result = 0

coin_list = [500, 100, 50, 10, 5, 1]

for coin in coin_list:
    if tot != 0:
        result += tot//coin
        tot = tot - coin * (tot//coin)
    else:
        break

print(result)

# %는 나눈 나머지
# // 는 몫