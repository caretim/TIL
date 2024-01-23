import sys

input = sys.stdin.readline

n, m = map(int, input().split())


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

matrix_1 = [list(input()) for __ in range(n)]

matrix_2 = [list(input()) for __ in range(n)]

visited = [[0] * m for __ in range(n)]


def bfs(y, x):
    q = list()
    q.append((y, x))
    check = []
    check.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.pop()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (
                0 <= ny < n
                and 0 <= nx < m
                and matrix_1[y][x] == matrix_1[ny][nx]
                and visited[ny][nx] == 0
            ):
                q.append((ny, nx))
                check.append((ny, nx))
                visited[ny][nx] = 1

    temp = matrix_2[y][x]
    while check:
        y, x = check.pop()
        if matrix_2[y][x] != temp:
            return False

    return True


for y in range(n):
    for x in range(m):
        if visited[y][x] == 0:
            if bfs(y, x) == False:
                print("NO")
                exit()

print("YES")
