n, m = map(int, input().split())


board = [[0] for __ in range(101)]

print(board)
good = []

bad = []

count = 0


for __ in range(n):
    x, y = map(int, input().split())
    board[x] = y
    if y - x > 6:
        good.append(x)

for __ in range(m):
    x, y = map(int, input().split())
    board[x] = y
    bad.append(x)


def throw(a):
    global count
    count += 1
    for i in range(6, 0, -1):
        if a + i == 100:
            return
        elif a + i in good:
            count += 1
            throw(board[a + i])
            return
        elif a + i in bad:
            pass
        else:
            count += 1
            throw(a + i)
            return


throw(1)
print(count)
