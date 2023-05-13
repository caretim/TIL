import heapq 

import sys

input = sys.stdin.readline
INF = sys.maxsize

m,n= map(int,input().split())

dy = [0,0,1,-1]
dx = [1,-1,0,0]

check_matrix=[[INF]*(m) for __ in range(n)]


matrix =[list(map(int,input().rstrip())) for __ in range(n)]

#리스트를 탐색하면서, 각 도착점에 오는동안 부순 벽의 횟수를 체크, 가장 적은값이어야함 

def dijkstra(y,x):
    q=[]
    heapq.heappush(q,(0,y,x))
    check_matrix[y][x]=0
    while q:
        j,y,x=heapq.heappop(q)

        if j>check_matrix[y][x]:
            continue
        for i in range(4):
            ny,nx= y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if matrix[ny][nx]==1:
                    if j+1<check_matrix[ny][nx]:
                        check_matrix[ny][nx] =j+1
                        heapq.heappush(q,(j+1,ny,nx))
                elif j<check_matrix[ny][nx]: # 0일 때 옆에도 0이라 계속 도는데 방문리스트처리..
                    check_matrix[ny][nx] = j  # 최소힙이라 가장 횟수가 적은것부터 시행,
                    heapq.heappush(q,(j,ny,nx))


dijkstra(0,0)
print(check_matrix[n-1][m-1])

