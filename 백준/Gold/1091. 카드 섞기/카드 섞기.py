import sys

input = sys.stdin.readline

dict = {}

n = int(input())


cards = list(map(int, input().split()))

for i in range(len(cards)):
    dict[i] = i % 3

change = list(map(int, input().split()))

flag = 1


def shuffle(cards):
    shu_card = [0] * (n)
    for i in range(n):
        shu_card[change[i]] = cards[i]
    return shu_card


cnt = 0
while flag:
    for i in range(n):
        if cards[i] != dict[i]:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        print(cnt)
        break
    cards = shuffle(cards)
    cnt += 1
    if cnt > 1000000:
        print(-1)
        break
