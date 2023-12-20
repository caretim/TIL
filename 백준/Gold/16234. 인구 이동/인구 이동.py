import sys
from collections import deque


input = sys.stdin.readline

N, L, R = map(int, input().split())

# 날이 바뀔 때 마다 모든 지역 방문해서 연합인 국가, visit을 계속 초기화

matrix = [list(map(int, input().split())) for __ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
flag = True
cnt = 0


def bfs(y, x, visited):
    visited[y][x] = 1
    change = [(y, x)]
    total = matrix[y][x]
    changeFlag = False
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # try:
            #     print(abs(matrix[ny][nx] - matrix[y][x]))
            # except:
            #     pass
            if (
                0 <= ny < N
                and 0 <= nx < N
                and visited[ny][nx] == 0
                and L <= abs(matrix[ny][nx] - matrix[y][x]) <= R
            ):
                total += matrix[ny][nx]
                visited[ny][nx] = 1
                q.appendleft((ny, nx))
                change.append((ny, nx))
                changeFlag = True
    if changeFlag == True:
        ave = total // len(change)
        for y, x in change:
            matrix[y][x] = ave
        return True
    else:
        return False


while flag:  # 종료 조건을 어떻게주지?
    dayFlag = False

    visited = [[0] * (N) for __ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                if bfs(y, x, visited):
                    dayFlag = True
                # print(matrix)
    if dayFlag == False:
        flag = False
    cnt += 1

# print(matrix)
print(cnt - 1)
