

import sys
import heapq

input = sys.stdin.readline

n= int(input())

INF = sys.maxsize

matrix = [list(map(int,input())) for __ in range(n)]

check_matrix = [[INF]*n for __ in range(n)]

dy,dx = [0,0,1,-1],[1,-1,0,0]


# 검은방 0 흰방 1 
def dijkstra(y,x):
    q = []
    heapq.heappush(q,(0,y,x)) #(부순벽의값,y,x)
    check_matrix[y][x]=0
    while q:
        j,y,x= heapq.heappop(q)
        if (y,x) == (n-1,n-1):
            return j
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if matrix[ny][nx]==0:
                    if j+1<check_matrix[ny][nx]:
                        check_matrix[ny][nx]=j+1
                        heapq.heappush(q,(j+1,ny,nx))
                elif matrix[ny][nx]==1:
                    if j<check_matrix[ny][nx]:
                        check_matrix[ny][nx]=j
                        heapq.heappush(q,(j,ny,nx))

print(dijkstra(0,0))


                


