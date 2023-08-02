import sys
import heapq
from copy import deepcopy
INF= sys.maxsize
input = sys.stdin.readline


dx,dy = [0,0,1,-1],[1,-1,0,0]

n= int(input())

#높이값(경사)은 절대값, 
# 이동중 최소 높이로 n,n에 도달하기위해선? 
matrix = [list(map(int,input().split()))  for __ in range(n)]


def dijstra(y,x):
    # visit =deepcopy(matrix)
    visit = [[INF]*(n) for __ in range(n)]
    q= []
    visit[y][x]=0
    heapq.heappush(q,(0,y,x))
    while q:
        max_w ,y,x = heapq.heappop(q)
        if visit[y][x]<max_w:
            continue
        if (y,x) == (n-1,n-1):
            return max_w
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=nx<n and 0<=ny<n:
                new_w = max(max_w,abs(matrix[y][x]-matrix[ny][nx]))
                if visit[ny][nx]>new_w:
                    visit[ny][nx]=new_w
                    heapq.heappush(q,(new_w,ny,nx))
    
                
print(dijstra(0,0))

