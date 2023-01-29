n, m, c = map(int, input().split())

matrix = [[0] * (m + 1) for __ in range(n + 1)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for __ in range(c):
    y, x = map(int, input().split())
    matrix[y][x] = 1

result = []


def dfs(y, x):
    global result
    count = 1
    stack = []
    stack.append((y, x))
    matrix[y][x] = -1
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n + 1 and 0 <= nx < m + 1:
                if matrix[ny][nx] == 1:
                    matrix[ny][nx] = -1
                    stack.append((ny, nx))
                    count += 1
    result.append(count)


for y in range(n + 1):
    for x in range(m + 1):
        if matrix[y][x] == 1:
            dfs(y, x)

if len(result) == 0:
    print(0)
else:
    print(max(result))



