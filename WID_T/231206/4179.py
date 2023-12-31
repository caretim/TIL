# https://www.acmicpc.net/problem/4179


import sys
from collections import deque

input = sys.stdin.readline

INF = sys.maxsize

r, c = map(int, input().split())

matrix = [list(input().rstrip()) for __ in range(r)]
visited = [[0] * (c) for __ in range(r)]

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
fire = deque()
for y in range(r):
    for x in range(c):
        if matrix[y][x] == "F":
            fire.append((y, x, 0))
            matrix[y][x] = 0

        if matrix[y][x] == "J":
            jy, jx = y, x
            matrix[y][x] = -1

        if matrix[y][x] == "#":
            matrix[y][x] = -1
        if matrix[y][x] == ".":
            matrix[y][x] = INF


def bfs(fire, jy, jx):
    q = fire
    while q:
        y, x, cnt = q.pop()
        cnt += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and matrix[ny][nx] == INF:
                matrix[ny][nx] = cnt
                q.appendleft((ny, nx, cnt))
    q = deque()
    q.append((jy, jx, 0))
    visited[jy][jx] = 1
    matrix[jy][jx] = 0
    while q:
        y, x, cnt = q.pop()
        cnt += 1
        for i in range(4):
            ny, nx = ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if visited[ny][nx] == 0 and matrix[ny][nx] > cnt:
                    visited[ny][nx] = cnt
                    q.appendleft((ny, nx, cnt))
            else:
                print(cnt)
                exit()
    return print("IMPOSSIBLE")


bfs(fire, jy, jx)
