from collections import deque
from copy import deepcopy

def bfs(y, x, n):
    q = deque()
    q.append((y, x))
    graph[y][x] = n
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < N) and (0 <= X < M) and graph[Y][X] == 'X':
                q.append((Y, X))
                graph[Y][X] = n
                
def bfs2(y, x):
    q = deque()
    q.append((y, x))
    a[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < N) and (0 <= X < M):
                if a[Y][X] == '2':
                    return a[y][x]
                if a[Y][X] == '.':
                    q.append((Y, X))
                    a[Y][X] = a[y][x]+1
    return -1

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'X':
            bfs(i, j, str(cnt))
            cnt += 1
res = N*M
for i in range(N):
    for j in range(M):
        if graph[i][j] == '1':
            a = deepcopy(graph)
            t = bfs2(i, j)
            if t > -1:
                res = min(res, t)
print(res)