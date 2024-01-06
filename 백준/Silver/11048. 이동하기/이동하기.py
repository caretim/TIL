import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for __ in range(n)]

visited = [[-1] * (m) for __ in range(n)]

# bfs방식 - 시간초과,
# q = deque()
# q.append((0, 0, matrix[0][0]))
# visited[0][0] = matrix[0][0]
# while q:
#     y, x, cnt = q.pop()
#     for ny, nx in ((y + 1, x), (y, x + 1), (y + 1, x + 1)):
#         if 0 <= ny < n and 0 <= nx < m:
#             if visited[ny][nx] < cnt + matrix[ny][nx]:
#                 visited[ny][nx] = cnt + matrix[ny][nx]
#                 q.appendleft((ny, nx, cnt + matrix[ny][nx]))

# dp방식 - 이동하며 주어진 값에  플러스만 해주면 됨,

for y in range(n):
    for x in range(m):
        if y == 0 and x == 0:
            visited[0][0] = matrix[0][0]
        elif y == 0:
            visited[y][x] = visited[y][x - 1] + matrix[y][x]
        elif x == 0:
            visited[y][x] = visited[y - 1][x] + matrix[y][x]
        else:
            visited[y][x] = max((visited[y - 1][x], visited[y][x - 1])) + matrix[y][x]

# print(visited)
print(visited[n - 1][m - 1])
