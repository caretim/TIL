from collections import deque



# cards = deque()


n= int(input())


card = [i for i in range(1,n+1)]

card = deque(card)

if len(card)==1:
    print(1)
    exit()

while True:
    card.popleft()
    c = card.popleft()
    card.append(c)
    if len(card)==1:
        break
print(card[0])