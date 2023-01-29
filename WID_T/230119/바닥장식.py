n, m = map(int, input().split())

matrix = [list(input()) for __ in range(n)]

check = [[0] * m for __ in range(n)]

ver = [1, -1]
hor = [1, -1]

result = n * m


def Horizon(y, x):
    global result
    matrix[y][x] = result
    stack = []
    stack.append(x)
    while stack:
        x = stack.pop()
        for i in range(2):
            nx = x + hor[i]
            if 0 <= nx < m:
                if (check[y][nx], matrix[y][nx]) == (0, "-"):
                    matrix[y][nx] = 0
                    check[y][nx] = 1
                    result -= 1
                    stack.append(nx)
def vertical(y, x):
    global result
    matrix[y][x] = 0
    stack = []
    stack.append(y)
    while stack:
        y = stack.pop()
        for i in range(2):
            ny = y + ver[i]
            if 0 <= ny < n:
                if (check[ny][x], matrix[ny][x]) == (0, "|"):
                    matrix[ny][x] = 0
                    check[ny][x] = 1
                    result -= 1
                    stack.append(ny)


for y in range(n):
    for x in range(m):
        if (check[y][x], matrix[y][x]) == (0, "-"):
            Horizon(y, x)
        elif (check[y][x], matrix[y][x]) == (0, "|"):
            vertical(y, x)

print(result)
