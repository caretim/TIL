n = int(input())

paper = [list(input().split()) for __ in range(n)]


result = [0, 0, 0]  # -1,0,1


def PaperSlice(m, x, y):
    check = paper[m][m]
    for y in range(m):
        for x in range(m):
            if paper[y][x] != check:
                pass
    return check
