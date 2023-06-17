import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize


dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]


def minus(x):
    x = x - 1
    return x


N = int(input())

ab = list(map(int, input().split()))

ax, ay, bx, by = map(minus, ab)

matrix = [list(map(int, input().split())) for __ in range(N)]

check = [[INF] * (N) for __ in range(N)]


def dijkstra(sx, sy, ex, ey):
    if matrix[sy][sx] == -1:
        return -1
    q = []
    check[sy][sx] = matrix[sy][sx]
    result = -1
    heapq.heappush(q, (matrix[sy][sx], sy, sx))
    while q:
        w, y, x = heapq.heappop(q)
        if check[y][x] < w:
            continue
        if (y, x) == (ey, ex):
            return w
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] > 0:
                people = check[y][x] + matrix[ny][nx]
                if people < check[ny][nx]:
                    check[ny][nx] = people
                    heapq.heappush(q, (people, ny, nx))
    return result


print(dijkstra(ax, ay, bx, by))
