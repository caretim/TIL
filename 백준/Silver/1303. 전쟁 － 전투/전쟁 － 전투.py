m, n = map(int, input().split())

matrix = [list(input()) for __ in range(n)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(y, x, j):
    power = 1
    stack = []
    stack.append((y, x))
    matrix[y][x] = 0
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == j:
                    matrix[ny][nx] = 0
                    power += 1
                    stack.append((ny, nx))
    return power * power


B = 0
W = 0

for y in range(n):
    for x in range(m):
        if matrix[y][x] == "W":
            W += dfs(y, x, "W")
        elif matrix[y][x] == "B":
            B += dfs(y, x, "B")

print(W, B)
