import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

matrix = [[0] * (501) for __ in range(501)]
check = [[INF] * (501) for __ in range(501)]


for __ in range(int(input())):
    DX1, DY1, DX2, DY2 = map(int, input().split())

    for y in range(min(DY1, DY2), max(DY1, DY2) + 1):
        for x in range(min(DX1, DX2), max(DX1, DX2) + 1):
            matrix[y][x] = 1

for __ in range(int(input())):
    DX1, DY1, DX2, DY2 = map(int, input().split())
    for y in range(min(DY1, DY2), max(DY1, DY2) + 1):
        for x in range(min(DX1, DX2), max(DX1, DX2) + 1):
            matrix[y][x] = -1


def dijkstra(y, x):
    q = []
    check[y][x] = 0
    heapq.heappush(q, (0, y, x))
    while q:
        count, y, x = heapq.heappop(q)
        if check[y][x] < count:
            continue
        if y == 500 and x == 500:
            return count
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 501 and 0 <= nx < 501:
                cost = count + matrix[ny][nx]
                if (
                    matrix[ny][nx] >= 0 and cost < check[ny][nx]
                ):  # 일반지역 또는 위험지역일떄, 카운트한 값과 현재 위치의 값을 더해서 cost로 정해줌
                    # 코스트 값이 check[ny][nx]의 값보다 적다면, ny,nx = cost 로 비용을 추가해줌,.
                    check[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))
    return -1


print(dijkstra(0, 0))

# print(matrix)


# print(check)
