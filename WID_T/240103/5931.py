from collections import deque
import sys
from copy import deepcopy

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([(x, y)])
    dp = [[-1] * M for _ in range(N)]
    dp[x][y] = 0
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if dp[nx][ny] == -1:
                if li[nx][ny] == "." or li[nx][ny] == 2:
                    dp[nx][ny] = dp[x][y] + 1
                    q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if dp[i][j] != -1 and dp[i][j] != 0:
                if li[i][j] == 2:
                    lst.append(dp[i][j] - 1)


def dfs(x, y, c):
    q = deque([(x, y)])
    visited[x][y] = True
    li[x][y] = c
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == False and l[nx][ny] == "X":
                li[nx][ny] = c
                visited[nx][ny] = True
                q.append((nx, ny))


N, M = map(int, input().split())
l = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    l.append(list(input[:M]))
li = deepcopy(l)
c = 1
for x in range(N):
    for y in range(M):
        if visited[x][y] == False and l[x][y] == "X":
            dfs(x, y, c)
            c += 1
lst = []
for x in range(N):
    for y in range(M):
        if li[x][y] == 1:
            bfs(x, y)

print(min(lst))
