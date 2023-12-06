r, c = map(int, input().split())


matrix = [list(input()) for __ in range(r)]


dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

cnt = 0


def eat(y, x):
    stack = []
    stack.append((y, x))
    matrix[y][x] = "."
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and matrix[ny][nx] == "#":
                stack.append((ny, nx))
                matrix[ny][nx] = "."


for y in range(r):
    for x in range(c):
        if matrix[y][x] == "#":
            cnt += 1
            eat(y, x)

print(cnt)
