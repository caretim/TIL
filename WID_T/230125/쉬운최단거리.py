from collections import deque

n,m= map(int,input().split())


matrix = [list(map(int,input().split())) for __ in range(n)]
check = [[0]*m  for __ in range(n)]


dx = [0,0,1,-1]
dy = [-1,1,0,0]


def bfs(y,x):
    check[y][x]=1
    matrix[y][x]=0
    q = deque()
    q.append((y,x,0))
    while q:
        y,x,j = q.popleft()
        for i in range(4):
            ny= y+dy[i]
            nx= x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if (check[ny][nx],matrix[ny][nx]) == (0,1):
                    matrix[ny][nx]=j+1
                    check[ny][nx]=1
                    q.append((ny,nx,j+1))
find = 0
for y in range(n):
    if find == 1:
        break
    for x in range(m):
        if matrix[y][x]==2:
            bfs(y,x)
            find=1
            break
            

for y in range(n):
    for x in range(m):
        if (check[y][x],matrix[y][x]) == (0,1):
            matrix[y][x]=-1
for r in matrix:
    print(*r)