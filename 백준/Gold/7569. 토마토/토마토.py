from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())


matrix = [[list(map(int, input().split())) for __ in range(n)] for __ in range(h)]

check = [[[0] * m for __ in range(n)] for __ in range(h)]


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
dz = [1, -1]


# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다
# , 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 3중for문 돌려서 익은토마토 덱에 넣고 bfs탐색진행해서 카운트 올리면서 진행 마지막에 0이 있는지 탐색 후 존재한다면 -1
deq = deque()

result = 0


def bfs():
    global result
    q = deque(deq)
    while q:
        y, x, z, j = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            nz = z
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[nz][ny][nx] == 0:
                    matrix[nz][ny][nx] = 1
                    q.append((ny, nx, nz, j + 1))
                    if result < j + 1:
                        result = j + 1
        for ii in range(2):
            ny = y
            nx = x
            nz = z + dz[ii]
            if 0 <= nz < h:
                if matrix[nz][ny][nx] == 0:
                    matrix[nz][ny][nx] = 1
                    q.append((ny, nx, nz, j + 1))
                    if result < j + 1:
                        result = j + 1


# 3중포문에서 z축을 따로 돌리기
for z in range(h):
    for y in range(n):
        for x in range(m):
            if matrix[z][y][x] == 1:
                deq.append((y, x, z, 0))


bfs()


for z in range(h):
    for y in range(n):
        for x in range(m):
            if matrix[z][y][x] == 0:
                result = -1


print(result)
