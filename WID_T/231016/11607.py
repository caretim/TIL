import heapq

import sys

input = sys.stdin.readline

INF = sys.maxsize

n,m= map(int,input().split())

dy,dx = [0,0,-1,1],[1,-1,0,0]

matrix = [list(map(int,input().rstrip())) for __ in range(n)]

visit = [[INF]*(m) for __ in range(n)]

visit[0][0]=0

heap = [] 
heapq.heappush(heap,(0,0,0))

result = 'IMPOSSIBLE'
while heap:
    cnt,y,x= heapq.heappop(heap)
    if y==n-1 and x == m-1:
        result=cnt
        break
    if matrix[y][x]==0:
        continue
    for i in range(4):
        ny= y+(dy[i]*matrix[y][x])
        nx =x+(dx[i]*matrix[y][x])
        if 0<=ny<n and 0<=nx<m:
            if visit[ny][nx]>cnt+1:
                visit[ny][nx]=cnt+1
                heapq.heappush(heap,(cnt+1,ny,nx))
    
print(result)
