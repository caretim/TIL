from collections import deque
m,n=map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int,input().split())))
def bfs(x,y):
	#01
    q=deque([(x,y)])
    graph[x][y]=0
    dx=[-1,1,0,0,-1,-1,1,1]
    dy=[0,0,-1,1,-1,1,-1,1]
    while q:
        x,y=q.popleft()
        for i in range(8):
        	#02
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append((nx,ny))
#03
ans=0
for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)
            ans+=1
print(ans)
