import sys

input = sys.stdin.readline

dict = {}

n = int(input())


cards = list(map(int, input().split()))

card = cards

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
    if cards == card:  # 제한말고 모든 사이클이 돌고나면 최초의 순서로 돌아오는걸 조건으로 -1 출력가능
        print(-1)
        break
