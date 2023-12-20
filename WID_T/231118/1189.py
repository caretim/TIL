import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

INF = sys.maxsize

matrix = [list(input()) for __ in range(r)]


def dfs(sy, sx):
    visited = [[INF] * c for __ in range(r)]
    stack = []
    stack.append((sy, sx, 0))
    visited[sy][sx] = 0
    result = 0
    while stack:
        y, x, cnt = stack.pop()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] >= cnt + 1:
                if (ny, nx) == (0, c - 1):
                    if visited[0][c - 1] > cnt + 1:
                        result = 1
                        visited[ny][nx] = cnt + 1
                    elif visited[0][c - 1] == cnt + 1:
                        result += 1
                    continue
                if matrix[ny][nx] == ".":
                    visited[ny][nx] = cnt + 1
                    stack.append((ny, nx, cnt + 1))
    return result


print(dfs(r - 1, 0))
