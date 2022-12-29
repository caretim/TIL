n = int(input())

matrix = [list(input()) for __ in range(n)]

check1 = [[0] * n for __ in range(n)]

check2 = [[0] * n for __ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


result = [0, 0]


def dfs_nor(y, x, rgb):
    stack = []
    stack.append((y, x))
    check1[y][x] = 1
    while stack:
        k = stack.pop()
        for i in range(4):
            ny = k[0] + dy[i]
            nx = k[1] + dx[i]
            if n <= ny or 0 > ny or n <= nx or 0 > nx:
                continue
            if check1[ny][nx] == 0 and matrix[ny][nx] == rgb:
                stack.append((ny, nx))
                check1[ny][nx] = 1


def dfs_han(y, x, rgb):
    if rgb == "R" or rgb == "G":
        rgb = ["R", "G"]
    stack = []
    stack.append((y, x))
    check2[y][x] = 1
    while stack:
        k = stack.pop()
        for i in range(4):
            ny = k[0] + dy[i]
            nx = k[1] + dx[i]
            if n <= ny or 0 > ny or n <= nx or 0 > nx:
                continue
            if check2[ny][nx] == 0 and matrix[ny][nx] in rgb:
                stack.append((ny, nx))
                check2[ny][nx] = 1


for y in range(n):
    for x in range(n):
        if check1[y][x] != 1:
            dfs_nor(y, x, matrix[y][x])
            result[0] += 1
        if check2[y][x] != 1:
            dfs_han(y, x, matrix[y][x])
            result[1] += 1
for i in result:
    print(i, end=" ")
