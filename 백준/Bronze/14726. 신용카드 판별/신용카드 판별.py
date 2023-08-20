t = int(input())
for _ in range(t):
    card = list(str(input()))
    for i in range(0, 15, 2):
        card[i] = str(int(card[i]) * 2)
        if int(card[i]) >= 10:
            card[i] = str(sum(map(int, str(card[i]))))

    total = sum(map(int, card))

    print("T" if total % 10 == 0 else "F")