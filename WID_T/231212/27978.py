import sys, heapq

from collections import deque

input = sys.stdin.readline


INF = sys.maxsize
# 최단경로 우선, 이후 같은 길이의 경로중 가중치가 적은것,

move = [
    (-1, 1),
    (0, 1),
    (1, 1),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (-1, 0),
]  # ,1,2 -> 오른쪽이동 비용 0

h, w = map(int, input().split())


matrix = [list(input().rstrip()) for __ in range(h)]

visited = [[INF] * (w) for __ in range(h)]


def dijkstra(sy, sx, ey, ex):
    visited[sy][sx] = 0
    q = []
    heapq.heappush(q, (0, sy, sx))
    result = -1
    while q:
        cnt, y, x = heapq.heappop(q)
        for i in range(8):
            if i < 3:
                next_cnt = cnt
            else:
                next_cnt = cnt + 1
            ny, nx = y + move[i][0], x + move[i][1]
            if (ny, nx) == (ey, ex):  # 종료조건
                return next_cnt
            if 0 <= ny < h and 0 <= nx < w and matrix[ny][nx] == ".":
                if visited[ny][nx] > next_cnt:
                    visited[ny][nx] = next_cnt
                    heapq.heappush(q, (next_cnt, ny, nx))
    # print(visited)
    return result


for y in range(h):
    for x in range(w):
        if matrix[y][x] == "K":
            sy, sx = y, x
        if matrix[y][x] == "*":
            ey, ex = y, x


print(dijkstra(sy, sx, ey, ex))
