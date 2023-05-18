import sys

import heapq

INF = sys.maxsize
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def dijkstra(sx, sy, ex, ey):
    check = [[INF] * (M) for __ in range(N)]
    check[sx][sy] = 0
    q = []
    heapq.heappush(q, (0, sx, sy))
    while q:
        w, x, y = heapq.heappop(q)
        if check[x][y] < w:
            continue
        for i in range(8):
            ny, nx = y + directions[i][0], x + directions[i][1]
            if 0 <= ny < N and 0 <= nx < M and matrix[nx][ny] >= 0:
                d = abs(
                    max(matrix[x][y], matrix[nx][ny])
                    - min(matrix[x][y], matrix[nx][ny])
                )
                cost = (d + 1) ** 2  # d == 0이면 1 아니라면 계산식 적용
                if check[nx][ny] > w + cost:
                    check[nx][ny] = w + cost
                    heapq.heappush(q, (w + cost, nx, ny))
    return check[ex][ey]


for i in range(int(input())):
    N, M = map(int, input().split())
    s_matrix = [list(input().rstrip()) for __ in range(N)]
    matrix = [[0] * (M) for __ in range(N)]
    sx, sy = map(int, input().split())

    max_num = 0
    ex, ey = 0, 0

    for y in range(N):
        for x in range(M):
            if s_matrix[x][y] == "#":
                matrix[x][y] = -1
            else:
                matrix[x][y] = int(s_matrix[x][y])
                if matrix[x][y] > max_num:
                    max_num = matrix[x][y]
                    ey, ex = y, x
    if s_matrix[sx][sy] == "#":
        print("NO")
        continue

    r = dijkstra(sx, sy, ex, ey)
    if r == INF:
        print("NO")
    else:
        print(r)
