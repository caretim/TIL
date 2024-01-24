import sys
from collections import deque

input =sys.stdin.readline


n,m= map(int,input().split())

sy,sx = map(int,input().split())

ey,ex = map(int,input().split())

prison = [list(map(int,input().split())) for __ in range(n)]


dx,dy= [0,0,-1,1],[1,-1,0,0]


def bfs(y,x):
    wall = [[0]*(m) for __ in range(n)]
    visited = [[0]*(m) for __ in range(n)]
    q= deque()
    q.append((y,x,1,0))
    visited[y][x]=1

    while q:
        y,x,magic,cnt = q.pop()
        if (y,x) == (ey-1,ex-1):
            print(cnt)
            return
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m: # 범위확인 
                if magic == 0:
                    if prison[ny][nx] == 0 and wall[ny][nx]==0:  #마법사용 이후
                        wall[ny][nx]=1
                        q.appendleft((ny,nx,magic,cnt+1))
                if magic == 1:
                    if prison[ny][nx] == 1 and wall[ny][nx]==0: # 마법사용
                        wall[ny][nx]=1
                        q.appendleft((ny,nx,magic-1,cnt+1))
                    elif prison[ny][nx]==0 and visited[ny][nx]==0:
                        visited[ny][nx]=1
                        q.appendleft((ny,nx,magic,cnt+1))
    return print(-1)

        
bfs(sy-1,sx-1)


