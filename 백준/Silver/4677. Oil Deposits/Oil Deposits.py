from collections import deque

dy = [1, 0, -1, -1, -1, 0, 1, 1]
dx = [1, 1, 1, 0, -1, -1, -1, 0]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = "*"
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if (0 <= ny < m) and (0 <= nx < n) and graph[ny][nx] == "@":
                q.append((ny, nx))
                graph[ny][nx] = "*"


while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break

    graph = [list(input()) for _ in range(m)]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == "@":
                bfs(i, j)
                cnt += 1
    print(cnt)
