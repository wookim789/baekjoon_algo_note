
# 0 <= 시간 <= 23
# 0 <= 분 <= 59
# 0 <= 초 <= 59


# 시간에 3이 있을때 # 시간에 3이 없을떄
# 분에 3이 있을 떄  # 분에 3이 없을떄
# 초에 3이 있을 때  # 초에 3이 없을떄

# 1
# 60
# 3600
# 3 13 23

if __name__ == "__main__":

    hour = int(input())
    result = 0
    for h in range(hour + 1):
        for m in range(60):
            for s in range(60):
                if '3' in str(h) + str(m) + str(s):
                    result += 1

    print(result)