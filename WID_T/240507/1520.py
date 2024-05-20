# import sys
# from collections import deque
# input= sys.stdin.readline
# from copy import deepcopy 

# dy,dx= [0,0,1,-1],[1,-1,0,0]

# n,m = map(int,input().split())
#  # 중첩되는 경로 도착시, 이미 진행한 경로를 또 지나가면서 탐색함,
#  # 경로중 분기점일떄 , 분리되어 도착하는 경로 수만 세어서 도착시
#  # 현재 도달가능 경로수 * 도착지점 도달 가능 경로수

# matrix = [list(map(int,input().split())) for __ in range(n)]
# dp = [[0]*(m) for __ in range(n)]
# visited = [[0]*(m) for __ in range(n)]

# def check_point(path_matrix,padd):
#     for py,px in path_matrix: # 경로 도달시 패스노드 체크
#        dp[py][px]+=padd # 현재 노드 도달 가능한 경로 모두 더해주기

    
# def bfs(sy,sx):
#     result = 0
#     stack = []
#     stack.append(((sy,sx,[(sy,sx)])))
#     while stack:
#         y,x,path_matrix = stack.pop()
#         for i in range(4):
#             ny,nx = y+dy[i],x+dx[i]
#             if 0<=ny<n and 0<=nx<m and matrix[ny][nx]<matrix[y][x]:
#                 visited[ny][nx] =1 
#                 if (ny,nx) == (n-1,m-1):
#                     check_point(path_matrix,1)
#                     result+=1
#                     continue
#                 if dp[ny][nx]>0:
#                     check_point(path_matrix,dp[ny][nx])
#                     result+=dp[ny][nx]
#                     continue
#                 next_path = deepcopy(path_matrix)
#                 next_path.append((ny,nx))
#                 stack.append((ny,nx,next_path))
#     return result
# print(bfs(0,0))
# # print(dp)

import sys
import heapq


dy,dx= [0,0,1,-1],[1,-1,0,0]

n,m = map(int,input().split())


matrix = [list(map(int,input().split())) for __ in range(n)]

visited = [[0] * m for __ in range(n)]

def bfs(sy,sx):
    q =[]
    heapq.heappush(q,(-matrix[sy][sx],sy,sx))
    visited[sy][sx]=1
    while q:
        now,y,x =heapq.heappop(q)
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and matrix[ny][nx]<matrix[y][x]:
                if visited[ny][nx]==0:
                    heapq.heappush(q,(-matrix[ny][nx], ny, nx))
                visited[ny][nx] += visited[y][x]

bfs(0,0)
# print(visited)
print(visited[n-1][m-1])