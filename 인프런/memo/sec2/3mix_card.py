# 카드 역배치

card = list(range(21))

for i in range(10):
    s, e = map(int, input().split())
    for j in range((e - s + 1) // 2):
        card[s + j], card[e - j] = card[e - j], card[s + j]

for i in range(1, 21):
    print(card[i] , end = ' ')
