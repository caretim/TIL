from heapq import heappush, heappop
import sys


input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, -1, -1, 0, 0, 1, 1, 1]  #
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

T = int(input())

for _ in range(T):
    w, h = map(int, input().split())  # w : 너비 / h : 높이
    matrix_temp = [list(input().strip()) for _ in range(h)]  # 높이만큼 input을 반복
    a, b = map(int, input().split())  # a(h) : 높이 / b(w) : 너비 -
    matrix = [[0 for _ in range(w)] for _ in range(h)]

    mx, my = 0, 0  # 최고 높이를 찾기 위한 변수
    for i in range(h):
        for j in range(w):
            if matrix_temp[i][j] != "#":
                matrix[i][j] = int(matrix_temp[i][j])
                if matrix[i][j] > matrix[mx][my]:
                    mx, my = i, j
            elif matrix_temp[i][j] == "#":
                matrix[i][j] = -1

    # if not matrix[a][b]:
    #     print("NO")
    #     continue

    visited = [[INF for _ in range(w)] for _ in range(h)]
    visited[a][b] = 0
    hq = []
    heappush(hq, (a, b, 0))

    while hq:
        x, y, cost = heappop(hq)

        if cost > visited[x][y]:
            continue

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] >= 0:
                d = max(matrix[nx][ny], matrix[x][y]) - min(
                    matrix[nx][ny], matrix[x][y]
                )

                if d == 0:
                    cur_c = 1
                else:
                    cur_c = (d + 1) ** 2
                    

                nc = cur_c + cost

                if visited[nx][ny] > nc:
                    visited[nx][ny] = nc
                    heappush(hq, (nx, ny, nc))

    if visited[mx][my] != INF:
        print(visited[mx][my])
    else:
        print("NO")