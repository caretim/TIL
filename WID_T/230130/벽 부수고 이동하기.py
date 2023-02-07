# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.


# 일단 최단거리 넣고 벽수고 이동했을시, 최단거리 기록?
# bfs탐색중 벽을 부쉈다? 그러면 인자 y,x,b 로 b를 벽을 부순인자로 넣기?
# 벽을 부순 인자가 있다면 벽을 만났을때 탐색 x  안부쉈다면 벽을 부수고 이동

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input())) for __ in range(n)]

check = [[0] * m for __ in range(n)]
wall_check = [[0] * m for __ in range(n)]


dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(n, m):
    q = deque()
    q.append((0, 0, 0, 1))
    check[0][0] = 1
    while q:
        y, x, b, c = q.popleft()
        if (y, x) == (n - 1, m - 1):
            return c
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny < n and 0 <= nx < m and check[ny][nx] == 0:
                if matrix[ny][nx] == 1 and b == 0:
                    q.append((ny, nx, b + 1, c + 1))
                    check[ny][
                        nx
                    ] = 1  # 벽부수고 방문한거랑 벽 안부수고 방문한거랑 확인해야함 어떻게 확인시켜주지? 조건분기시킬까?
                elif matrix[ny][nx] == 0 and b == 1:  # 벽부수나서 0이동할때
                    if wall_check[ny][nx] == 0:
                        q.append((ny, nx, b, c + 1))
                        wall_check[ny][nx] = 1
                elif matrix[ny][nx] == 0 and b == 0:  # 벽을 안부순 상태에서 이동 할 떄
                    q.append((ny, nx, b, c + 1))
                    check[ny][nx] = 1  # 나중에 시행됬다면 어차피 안부수고 먼저 지나간경우가 먼저 체크될 것 임

    return -1


print(bfs(n, m))

for k in check:
    print(k)


# 3 6
# 010000
# 010111
# 000110


import sys

input = sys.stdin.readline


N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 2
que = [(0, 0)]
min_cnt = 1000000
cnt = 0

while que:
    cnt += 1  # 반복될때마다 cnt +1
    temp = []
    for r, c in que:
        if r == N - 1 and c == M - 1:
            min_cnt = cnt
            break

        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if (
                    visited[nr][nc] < visited[r][c] and arr[nr][nc] == "0"
                ):  # 2보다 작다가 흠.. 비짓 최초를 왜 2로 지정했을까?  0,1 구분해주기위해? 2
                    temp.append((nr, nc))
                    visited[nr][nc] = visited[r][c]  # 벽을 안뚫었다면 2로 방문처리

                elif (
                    visited[r][c] > 1 and arr[nr][nc] == "1"
                ):  # 한번도 방문하지 않은 벽을 만났을때  벽을 뚫고 만났다면 시작 visit[r][c]는 1이기에 진행안됨, 벽 1번 이상방지
                    temp.append((nr, nc))
                    visited[nr][nc] = (
                        visited[r][c] - 1
                    )  # 벽을 뚫었다면 1로 방문처리, if문 숫자비교로 일반방문 벽뚫방문 비교해주는 방법 기억하자

    else:
        que = temp
        continue

    break

print(min_cnt if min_cnt < 1000000 else -1)
