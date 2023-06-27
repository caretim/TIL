import sys
from collections import deque

input= sys.stdin.readline

n,m= map(int,input().split())


matrix =[[] for __ in range(n)]


dy,dx=[0,0,1,-1],[1,-1,0,0]

for i in range(n):
    matrix[i]=input().rstrip()

start_list =[]


for i in range(m):
    if matrix[0][i] =='0':
        start_list.append((0,int(i)))


def bfs(start_list):
    visit =[[0]*(m) for __ in range(n)]
    result = 'NO'
    q=deque()
    for sy,sx in start_list:
       visit[sy][sx]=1
       q.append((sy,sx))
    while q:
        y,x = q.popleft()
        if y == n-1:
           return print('YES')
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visit[ny][nx]==0 and matrix[ny][nx]=='0':
                    visit[ny][nx]=1
                    q.appendleft((ny,nx))
    print(result)

bfs(start_list)