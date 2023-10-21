import sys
from collections import deque

input = sys.stdin.readline


while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    matrix = [[] for __ in range(L)]

    start_find = 0
    for i in range(L):
        for j in range(R + 1):
            a = list(input().rstrip())
            if j == R:
                break
            if start_find == 0:
                if "S" in a:
                    for k in range(C):
                        if a[k] == "S":
                            sz, sy, sx = i, j, k
                            start_find = 1
            matrix[i].append(a)

    dz = [0, 0, 0, 0, -1, 1]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [1, -1, 0, 0, 0, 0]

    def bfs(z, y, x):
        result = "Trapped!"
        visit = [[[0] * (C) for __ in range(R)] for __ in range(L)]
        q = deque()
        q.append((z, y, x, 1))
        visit[z][y][x] = 1
        flag = 0
        while q:
            if flag == 1:
                break
            z, y, x, cnt = q.popleft()
            for i in range(6):
                nz = z + dz[i]
                ny = y + dy[i]
                nx = x + dx[i]
                if (
                    0 <= nz < L
                    and 0 <= ny < R
                    and 0 <= nx < C
                    and visit[nz][ny][nx] == 0
                ):
                    if matrix[nz][ny][nx] == ".":
                        visit[nz][ny][nx] = 1
                        q.append((nz, ny, nx, cnt + 1))
                    elif matrix[nz][ny][nx] == "E":
                        result = f"Escaped in {cnt} minute(s)."
                        flag = 1


        # for i in visit:
        #     for v in i:
        #         print(v)
        return result

    print(bfs(sz, sy, sx))
