import sys
sys.setrecursionlimit(10 ** 6)

input= sys.stdin

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def dfs(a, b):
    global trigger
    visited[a][b] = True

    # 8가지 방향 탐색
    for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]

        # 맵 안에 있으면
        if -1 < nx < n and -1 < ny < m:
            # 주변 산봉우리보다 작으면 False
            if graph[a][b] < graph[nx][ny]:
                trigger = False
            # 같은 높이의 산봉우리 탐색
            if not visited[nx][ny] and graph[nx][ny] == graph[a][b]:
                dfs(nx, ny)

n, m = map(int,input.split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 탐색 여부
visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        # 산봉우리가 0보다 크고 탐색하지 않았다면
        if graph[i][j] > 0 and not visited[i][j]:
            trigger = True
            dfs(i, j)

            # 산봉우리이면 카운트
            if trigger:
                cnt += 1

print(cnt)