from collections import deque
from copy import deepcopy
from pprint import pprint

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(input())


matrix = [list(map(int, input().split())) for __ in range(n)]


# 먼저 매트릭스 범위중 제일 큰 값 찾기

# 0~제일 큰 값 범위 확인 후 for문으로 탐색 진행 ,

result = []


def bfs(y, x, rain):
    check[y][x] = -1
    q = deque()
    q.append((y, x))
    while q:
        k = q.popleft()
        for j in range(4):
            ny = k[0] + dy[j]
            nx = k[1] + dx[j]
            if 0 <= ny < n and 0 <= nx < n:
                if check[ny][nx] > rain:
                    check[ny][nx] = -1
                    q.append((ny, nx))


max_vlaue = max(map(max, matrix))

for rain in range(0, max_vlaue):
    check = deepcopy(matrix)
    cnt = 0
    for y in range(n):
        for x in range(n):
            if check[y][x] > rain:
                cnt += 1
                bfs(y, x, rain)

    result.append(cnt)

print(max(result))
