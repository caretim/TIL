import heapq

import sys

input = sys.stdin.readline


def check_high(alp):
    if alp.isupper():  # 대문자일때는A값에서 빼주기,
        return ord(alp) - ord("A")
    else:  # 소문자는 a값에서 뺴주기 ,
        return ord(alp) - ord("a") + 26


INF = sys.maxsize


N, M, T, D = map(int, input().split())
# T는 이동 할 수 있는 높이, D는 어두워지는시간,
mountain = [list(map(check_high, input().rstrip())) for __ in range(N)]


time = []

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def dijkstra(y, x):
    matrix = [[INF] * (M) for _ in range(N)]
    q = []
    matrix[y][x] = 0
    heapq.heappush(q, (0, y, x))
    result = 0
    while q:
        t, y, x = heapq.heappop(q)
        if result < mountain[y][x]:
            result = mountain[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and T >= abs(mountain[y][x] - mountain[ny][nx])
            ):
                if matrix[ny][nx] < t:
                    continue
                if mountain[y][x] < mountain[ny][nx]:  # 높을때 .
                    nt = mountain[ny][nx] - mountain[y][x]
                    nt = nt * nt
                elif mountain[y][x] >= mountain[ny][nx]:  # 낮거나 같을때.
                    nt = 1
                if nt + t <= D and matrix[ny][nx] > nt + t:
                    matrix[ny][nx] = t + nt
                    heapq.heappush(q, (t + nt, ny, nx))
    return matrix


temp1 = dijkstra(0, 0)  # 호텔에서 산 등반,
# print(temp1)
temp2 = []  # 각 산의 높이에서 도착하는곳,

for y in range(N):
    for x in range(M):
        if temp1[y][x] <= D:
            heapq.heappush(temp2, (-1 * (mountain[y][x]), y, x))

while temp2:
    t, y, x = heapq.heappop(temp2)
    temp3 = dijkstra(y, x)
    if temp3[0][0] + temp1[y][x] <= D:
        print(mountain[y][x])
        # print(temp3[0][0] + temp1[y][x])
        break
