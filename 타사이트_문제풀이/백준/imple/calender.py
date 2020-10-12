# 달력

# 1, 3, 5, 7, 8, 10, 12 : 31
# 4, 6, 9, 11 : 30
# 2 : 28

calender = {1:31, 2:28, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31, 4:30, 6:30, 9:30, 11:30 }

week =['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

M, D = map(int, input().split())

date = 0
for m in range(1, M):
    date += calender[m]
date += D

print(week[(date % 7) - 1])


