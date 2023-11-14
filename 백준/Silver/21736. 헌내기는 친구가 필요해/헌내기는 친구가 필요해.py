from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(str, input().rstrip())))

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

cnt = 0
sx, sy = -1, -1

visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "I":
            sx, sy = i, j
            visited[sx][sy] = 1
        if matrix[i][j] == "X":
            visited[i][j] = 1

q = deque([(sx, sy)])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + directions[i][0], y + directions[i][1]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if matrix[nx][ny] == "P":
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
            elif matrix[nx][ny] == "O":
                visited[nx][ny] = 1
                q.append((nx, ny))

if cnt == 0:
    print("TT")
else:
    print(cnt)
