from collections import deque



cards = deque()


n= int(input())


for card in range(1,n+1):
    cards.append(card)

print(cards)

while True:
    cards.popleft()
    c = cards.popleft()
    cards.append(c)
    if len(cards)==1:
        break
print(cards[0])