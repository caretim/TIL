
import sys
from collections import deque
n = int(input())

move = [[-2,-1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
sy,sx,ey,ex = map(int,input().split())


INF = sys.maxsize
visited= [[INF]*(n) for __ in range(n)]


q = deque()

q.append((sy,sx,0))

visited[sy][sx] = 1
result= -1
while q:
    y,x,cnt = q.pop()
    if (y,x) == (ey,ex):
        print(cnt)
        exit()
    for i in range(6):
        ny,nx = y+move[i][0],x+move[i][1]
        if 0<=ny<n and 0<=nx<n and visited[ny][nx]>cnt:
            visited[ny][nx]=cnt
            q.appendleft((ny,nx,cnt+1))


print(result)