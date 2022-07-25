n = int(input())

for i in range(1, n + 1):
    i = str(i)
    game = i.count('3') + i.count('6') + i.count('9')
    if game == 0:
        print(i, end=' ')
    else:
        print('-'*game, end=' ')