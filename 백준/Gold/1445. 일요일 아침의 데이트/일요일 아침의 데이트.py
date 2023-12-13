import sys, heapq

input = sys.stdin.readline


dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

INF = sys.maxsize

n, m = map(int, input().split())

matrix = [list(input().rstrip()) for __ in range(n)]

visited = [[(INF, INF) for __ in range(m)] for __ in range(n)]


def checkTrash(y, x):
    for i in range(4):
        cy, cx = y + dy[i], x + dx[i]
        if 0 <= cy < n and 0 <= cx < m:
            if matrix[cy][cx] == "g":
                return False
    return True


def dijkstra(sy, sx):
    heap = []
    visited[sy][sx] = (0, 0)
    heapq.heappush(heap, ((0, 0, sy, sx)))
    while heap:
        trash, side, y, x = heapq.heappop(heap)
        # if visited[y][x] <= trash:
        #     continue
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == "F":  # 종료조건
                    # for v in visited:
                    #     print(v)
                    # print(ny, nx)
                    return trash, side
                if matrix[ny][nx] == "g":
                    if visited[ny][nx][0] > trash + 1:
                        visited[ny][nx] = (trash + 1, side)
                        heapq.heappush(heap, (trash + 1, side, ny, nx))
                    elif visited[ny][nx][0] == trash + 1 and visited[ny][nx][1] > side:
                        visited[ny][nx] = (trash + 1, side)
                        heapq.heappush(heap, (trash + 1, side, ny, nx))

                if matrix[ny][nx] == ".":
                    new_side = side
                    if not checkTrash(ny, nx):
                        new_side += 1
                    if visited[ny][nx][0] > trash:  # . 지나갈때
                        visited[ny][nx] = (trash, new_side)
                        heapq.heappush(heap, (trash, new_side, ny, nx))
                    elif visited[ny][nx][0] == trash and visited[ny][nx][1] > side:
                        visited[ny][nx] = (trash, new_side)
                        heapq.heappush(heap, (trash, new_side, ny, nx))


for y in range(n):
    for x in range(m):
        if matrix[y][x] == "S":
            print(*dijkstra(y, x))
            # for v in visited:
            #     print(v)
