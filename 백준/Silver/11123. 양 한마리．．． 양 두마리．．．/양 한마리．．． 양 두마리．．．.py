from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = "."
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (0 <= ny < H) and (0 <= nx < W) and graph[ny][nx] == "#":
                q.append((ny, nx))
                graph[ny][nx] = "."


for __ in range(int(input())):
    H, W = map(int, input().split())
    graph = [list(input()) for _ in range(H)]
    cnt = 0 
    for y in range(H):
        for x in range(W):
            if graph[y][x] == "#":
                bfs(y, x)
                cnt += 1
    print(cnt)
