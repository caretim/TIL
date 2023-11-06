from collections import deque


def bfs(x, y):
    sheep, wolf = 0, 0
    q.append((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        if matrix[x][y] == "v":
            wolf += 1
        elif matrix[x][y] == "k":
            sheep += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < r
                and 0 <= ny < c
                and matrix[nx][ny] != "#"
                and visit[nx][ny] == 0
            ):
                visit[nx][ny] = 1
                q.append((nx, ny))
    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0
    return sheep, wolf


r, c = map(int, input().split())


visit = [[0] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

rs, rw = 0, 0
matrix = [list(input().rstrip()) for __ in range(r)]

for i in range(r):
    for j in range(c):
        if matrix[i][j] in ("v", "k") and visit[i][j] == 0:
            s, w = bfs(i, j)
            rs += s
            rw += w
print(rs, rw)
