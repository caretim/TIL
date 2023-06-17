from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def check_R(x, y):
    return -1 < x < n and -1 < y < m


def bfs(a, b):
    queue = deque()
    visit = [[0] * m for i in range(n)]

    queue.append([a, b])
    visit[a][b] = 1
    count = -1
    while queue:
        size = len(queue)
        for _ in range(size):
            a, b = queue.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if not check_R(nx, ny) or visit[nx][ny] or matrix[nx][ny] == "W":
                    continue
                visit[nx][ny] = 1
                queue.append((nx, ny))
        count += 1
    return count


n, m = map(int, input().split())
matrix = [input() for __ in range(n)]


result = 0
for x in range(n):
    for y in range(m):
        if matrix[x][y] == "L":
            result = max(result, bfs(x, y))
print(result)
