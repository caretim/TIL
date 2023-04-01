from collections import deque


# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면,
# 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다.
# 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다.
# 물고기를 먹으면, 그 칸은 빈 칸이 된다.
# 크기에 따라 먹는 물고기 수 증가 2일때는 물고기 2마리 먹어야 크기 +1  ex ) 5일떄는 5마리


# 같은 물고기를 먹을 수 있을때 거리비교,
# 물고기 최단거리를 어떻게 ?

n = int(input())
dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]

fish = [[] for __ in range(7)]

matrix = [list(map(int, input().split())) for __ in range(n)]

for y in range(n):
    for x in range(n):
        if matrix[y][x] == 9:
            sy, sx = y, x
            matrix[y][x] = 0
#             continue
#         if matrix[y][x] != 0:
#             fish[(matrix[y][x])].append((y, x))
# sorted(eat_range,key =lambda x: x1:x2:)


def hunting(y, x):
    check = [[0] * n for __ in range(n)]
    baby_shark = 2  # 상어크기
    eat_fish = 0  # 먹은 물고기 수
    result = 0
    q = deque()
    q.append((y, x, 2, 0))
    check[y][x] = 1
    while q:
        y, x, r, count = q.popleft()
        count += 1
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny < n and 0 <= nx < n and check[ny][nx] == 0:
                if (
                    matrix[ny][nx] == 0 or matrix[ny][nx] == baby_shark
                ):  # 지나가는 경로가 0이거나 크기가 같을 때,
                    check[ny][nx] = 1
                    q.append((ny, nx, r, count))
                elif (
                    0 < matrix[ny][nx] < baby_shark
                    and check[ny][nx] == 0  # 자기보다 낮을 물고기 먹었을때,
                ):  # 0이 아닌 물고기일때.
                    eat_fish += 1  # 먹은 물고기 +1
                    matrix[ny][nx] = 0  # 물고기 지워주기
                    check = [[0] * n for __ in range(n)]
                    if eat_fish == baby_shark:  # 만약 먹은 물고기 수가 크기와 같다면 크기 증가 (체크리스트 초기화)
                        baby_shark += 1
                        eat_fish = 0
                    q = deque()
                    result = count
                    q.append((ny, nx, r + 1, count))
    return result


# 먹을 물고기 찾는 함수 ,
# 물고기를 찾아가는 함수,
# 두개로 진행,

print(hunting(sy, sx))
