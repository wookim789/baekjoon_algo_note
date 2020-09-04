# 역순으로 -1씩 줄여가며 순회하는 기법

for i in range(10):
    for j in range(i, 0, -1):
        print(j, end = ' ')
    print()