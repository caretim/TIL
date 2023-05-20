# import sys
# from collections import deque

# input = sys.stdin.readline


# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, 1, -1, -1, 0, 1]

# n, m = map(int, input().split())

# matrix = [(list(map(int, input().split()))) for __ in range(n)]


# check = [[0] * m for __ in range(n)]

# cnt = 0


# def bfs(x, y):
#     global checker
#     check[y][x] = 1
#     for i in range(8):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= ny < n and 0 <= nx < m:
#             if matrix[y][x] < matrix[ny][nx]:
#                 checker == 1
#                 return 0
#             if check[y][x] == 0 and matrix[y][x] == matrix[nx][ny]:
#                 bfs(x, y)


# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > 0 and check[i][j] == 0:
#             checker = 0
#             bfs(i, j)
#             if checker == 0:
#                 cnt += 1


# print(cnt)


# import sys

# sys.setrecursionlimit(10**6)


# # dfs 탐색
# def dfs(a, b):
#     # 상/하/좌/우/대각선 확인
#     dx = [1, -1, 0, 0, 1, 1, -1, -1]
#     dy = [0, 0, 1, -1, 1, -1, -1, 1]

#     # 산봉우리인지 체크
#     global trigger

#     # 탐색 체크
#     visited[a][b] = True

#     # 8가지 방향 탐색
#     for i in range(8):
#         x = a + dx[i]
#         y = b + dy[i]

#         # 맵 안에 있으면
#         if -1 < x < n and -1 < y < m:
#             # 주변 산봉우리보다 작으면 False
#             if graph[a][b] < graph[x][y]:
#                 trigger = False
#             # 같은 높이의 산봉우리 탐색
#             if not visited[x][y] and graph[x][y] == graph[a][b]:
#                 dfs(x, y)


# n, m = map(int, sys.stdin.readline().split())
# # 2차원 그래프를 표현
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# # 탐색 여부
# visited = [[False] * m for _ in range(n)]
# cnt = 0

# for i in range(n):
#     for j in range(m):
#         # 산봉우리가 0보다 크고 탐색하지 않았다면
#         if graph[i][j] > 0 and not visited[i][j]:
#             trigger = True
#             dfs(i, j)

#             # 산봉우리이면 카운트
#             if trigger:
#                 cnt += 1

# print(cnt)

# import sys
# from collections import deque

# input = sys.stdin.readline


# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, 1, -1, -1, 0, 1]

# n, m = map(int, input().split())

# matrix = [(list(map(int, input().split()))) for __ in range(n)]


# check = [[0] * m for __ in range(n)]

# cnt = 0


# def bfs(x, y):
#     global checker
#     check[y][x] = 1
#     for i in range(8):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= ny < n and 0 <= nx < m:
#             if matrix[y][x] < matrix[ny][nx]:
#                 checker == 1
#                 return 0
#             if check[y][x] == 0 and matrix[y][x] == matrix[nx][ny]:
#                 bfs(x, y)


# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > 0 and check[i][j] == 0:
#             checker = 0
#             bfs(i, j)
#             if checker == 0:
#                 cnt += 1


# print(cnt)


# import sys

# sys.setrecursionlimit(10**6)


# # dfs 탐색
# def dfs(a, b):
#     # 상/하/좌/우/대각선 확인
#     dx = [1, -1, 0, 0, 1, 1, -1, -1]
#     dy = [0, 0, 1, -1, 1, -1, -1, 1]

#     # 산봉우리인지 체크
#     global trigger

#     # 탐색 체크
#     visited[a][b] = True

#     # 8가지 방향 탐색
#     for i in range(8):
#         x = a + dx[i]
#         y = b + dy[i]

#         # 맵 안에 있으면
#         if -1 < x < n and -1 < y < m:
#             # 주변 산봉우리보다 작으면 False
#             if graph[a][b] < graph[x][y]:
#                 trigger = False
#             # 같은 높이의 산봉우리 탐색
#             if not visited[x][y] and graph[x][y] == graph[a][b]:
#                 dfs(x, y)


# n, m = map(int, sys.stdin.readline().split())
# # 2차원 그래프를 표현
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# # 탐색 여부
# visited = [[False] * m for _ in range(n)]
# cnt = 0

# for i in range(n):
#     for j in range(m):
#         # 산봉우리가 0보다 크고 탐색하지 않았다면
#         if graph[i][j] > 0 and not visited[i][j]:
#             trigger = True
#             dfs(i, j)

#             # 산봉우리이면 카운트
#             if trigger:
#                 cnt += 1

# print(cnt)


import sys
input=sys.stdin.readline
from collections import deque

n, m=map(int, input().split())
data=[] 
for i in range(n):
    data.append(list(map(int, input().split())))

dx=[-1,-1,-1,0,0,1,1,1] 
dy=[-1,0,1,1,-1,-1,0,1]

checkidx=[]

def bfs(x, y, checkidx):
    q=deque([(x,y)])
    visited[x][y]=1
    check=[(x, y)]
    while q:
        X, Y= q.popleft()
        for i in range(8):
            nx, ny= X+dx[i], Y+dy[i] 
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if visited[nx][ny]==1:
                continue
            if data[X][Y]<data[nx][ny]:
                return 0
            if data[X][Y]==data[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                check.append((nx,ny))
        checkidx+=check 
    return 1

cnt=0
for i in range(n):
    for j in range(m):
        if (i, j) not in checkidx:
            visited=[[0]*m for _ in range(n)]
            cnt+=bfs(i,j,checkidx)
print(cnt)