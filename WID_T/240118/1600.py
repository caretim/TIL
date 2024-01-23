import sys

from collections import deque

input = sys.stdin.readline

m_move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

h_move = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]

k = int(input())

w, h = map(int, input().split())


matrix = [list(map(int, input().split())) for __ in range(h)]

visited = [[-1] * (w) for __ in range(h)]

q = deque()
q.append((0, 0, 0, k))
result = -1

while q:
    y, x, cnt, ck = q.pop()
    if y == h - 1 and x == w - 1:
        result = cnt
        break

    if ck > 0:
        for dy, dx in h_move:
            ny, nx = dy + y, dx + x
            if (
                0 <= ny < h
                and 0 <= nx < w
                and visited[ny][nx] < ck - 1
                and matrix[ny][nx] != 1
            ):
                visited[ny][nx] = ck - 1
                q.appendleft((ny, nx, cnt + 1, ck - 1))

    for dy, dx in m_move:
        ny, nx = dy + y, dx + x
        if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] < ck and matrix[ny][nx] != 1:
            visited[ny][nx] = ck
            q.appendleft((ny, nx, cnt + 1, ck))

# for v in visited:
#     print(v)
print(result)
