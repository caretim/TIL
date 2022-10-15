# dfs

# 델타 8방위 탐색 좌표
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

# 지도에 섬이 발견되었다면 dfs 시행
def dfs(y, x):
    land[y][x] = 0  # 땅의 위치를 방문처리
    stack = []
    stack.append((y, x))  # 튜플로 스택에 넣는다.
    while stack:
        k = stack.pop()  # 스택은 후입선출의 특성을 가지므로 마지막에 들어간 값을 꺼내서 델타탐색을 진행한다.
        for i in range(8):
            ny = dy[i] + k[0]
            nx = dx[i] + k[1]
            if ny >= n or ny < 0 or nx >= m or nx < 0:
                continue
            if land[ny][nx] == 1:
                land[ny][nx] = 0
                stack.append((ny, nx))
    return 1


while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:  # 입력이 0, 0이면 입력의 마지막줄이므로 반복문 중지
        break
    land = [list(map(int, input().split())) for __ in range(n)]  # 방문리스트 설정
    cnt = 0  # 섬의 갯수를 카운트한다.
    for y in range(n):  # 지도의 좌표를 모두 확인하며 땅을 확인한다 좌표가 1일 때 dfs탐색을 실행시킨다.
        for x in range(m):
            if land[y][x] == 1:
                dfs(y, x)
                cnt += 1
    print(cnt)


# bfs
from collections import deque

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(y, x):
    land[y][x] = 0
    q = deque()
    q.append((y, x))
    while q:
        k = q.popleft()
        for i in range(8):
            ny = k[0] + dy[i]
            nx = k[1] + dx[i]
            if ny >= n or ny < 0 or nx >= m or nx < 0:
                continue
            if land[ny][nx] == 1:
                land[ny][nx] = 0
                q.append((ny, nx))
    return 1


while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:  # 입력이 0, 0이면 입력의 마지막줄이므로 반복문 중지
        break
    land = [list(map(int, input().split())) for __ in range(n)]  # 방문리스트 설정
    cnt = 0  # 섬의 갯수를 카운트한다.
    for y in range(n):  # 지도의 좌표를 모두 확인하며 땅을 확인한다 좌표가 1일 때 dfs탐색을 실행시킨다.
        for x in range(m):
            if land[y][x] == 1:
                bfs(y, x)
                cnt += 1
    print(cnt)
