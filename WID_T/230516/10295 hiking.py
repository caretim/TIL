import sys

import heapq

INF = sys.maxsize
input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def dijkstra(sx, sy, ex, ey):
    check = [[INF] * (M) for __ in range(N)]
    check[sy][sx] = 0
    q = []
    result = "NO"
    heapq.heappush(q, (0, sy, sx))
    while q:
        w, y, x = heapq.heappop(q)
        if check[y][x] < w:
            continue
        for i in range(8):
            ny, nx = y + directions[i][0], x + directions[i][1]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] >= 0:
                d = abs(
                    max(matrix[y][x], matrix[ny][nx])
                    - min(matrix[y][x], matrix[ny][nx])
                )
                cost = 1 if d == 0 else (d + 1) ** 2  # d == 0이면 1 아니라면 계산식 적용
                if check[ny][nx] > w + cost:
                    check[ny][nx] = w + cost
                    heapq.heappush(q, (w + cost, ny, nx))
    for c in check:
        print(c)
    return check[ey][ex]


for i in range(int(input())):
    N, M = map(int, input().split())
    s_matrix = [list(input().rstrip()) for __ in range(N)]
    matrix = [[0] * (M) for __ in range(N)]
    sx, sy = map(int, input().split())

    max_num = 0
    ex, ey = 0, 0

    for y in range(N):
        for x in range(M):
            if s_matrix[y][x] == "#":
                matrix[y][x] = -1
            else:
                matrix[y][x] = int(s_matrix[y][x])
                if matrix[y][x] > max_num:
                    max_num = matrix[y][x]
                    ey, ex = y, x
    if s_matrix[sx][sy] == "#":
        print("NO")
        continue

    r = dijkstra(sx, sy, ex, ey)
    if r == INF:
        print("NO")
    else:
        print(r)
