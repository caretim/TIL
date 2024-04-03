# import heapq
# import sys

# input = sys.stdin.readline


# INF= sys.maxsize

# dy,dx = [0,0,1,-1],[1,-1,0,0]

# n,t=map(int,input().split())

# matrix=[list(map(int, input().split())) for __ in range(n)]

# dp=[[[INF]*(n) for __ in range(n)] for __ in range(3)]

# def dijkstra(y,x):
#     heap=[]
#     # dp[0][0][0] =0
#     heapq.heappush(heap,(0,y,x,0)) #시간 , 위치 , 이동횟수
#     # result = INF

#     while heap:
#         time,y,x,cnt = heapq.heappop(heap)
#         time+=2
#         if dp[cnt][y][x]<time:
#             continue
#         # if (y,x) == (n-1,n-1):
#         #     result = min(result,time)
#         #     print(result,time, '값찾음')
#         #     continue
#         for i in range(4):
#             ny,nx = y+dy[i],x+dx[i]
#             if 0<=ny<n and 0<=nx<n:
#                 if cnt ==2:
#                     if dp[cnt][ny][nx]> time+matrix[ny][nx]:
#                         dp[cnt][ny][nx] = time +matrix[ny][nx]
#                         heapq.heappush(heap,(time+matrix[ny][nx],ny,nx,0))
#                 else:
#                     if dp[cnt][ny][nx]> time:
#                         dp[cnt][ny][nx] = time
#                         heapq.heappush(heap,(time,ny,nx,cnt+1))
#     result = INF
#     print(dp)
#     for i in range(3):
#         result = min(result, dp[i][-1][-1], 
#             dp[i][-2][-1] + t, dp[i][-1][-2],
#             dp[i][-3][-1] + 2*t, dp[i][-2][-2] + 2*t, dp[i][-1][-3] + 2*t
#         )
#     return result

# print(dijkstra(0,0))

import  heapq
import sys

INF = sys.maxsize



dy = [0,  0,  1, -1,  3,  2,  1,  0, -1, -2, -3, -2, -1,  0,  1,  2]
dx = [1, -1,  0,  0,  0,  1,  2,  3,  2,  1,  0, -1, -2, -3, -2, -1]


input = sys.stdin.readline
N, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def dijkstra(y,x):
    heap = []
    heapq.heappush(heap, (0, y, x, 0))
    
   
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = 0
    result = INF
    
    while heap:
        d, c, x, y = heapq.heappop(heap)
        
        if visited[x][y] < d: continue
        
        remain = (N-1-x) + (N-1-y)
        
        if remain <= 2:
            result = min(result, d + remain * T)
            
        for k in range(16):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N:
                cost = matrix[nx][ny] + d + 3 * T
                
                if visited[nx][ny] > cost:
                    visited[nx][ny] = cost
                    heapq.heappush(heap, (cost, c + 1, nx, ny))

    return result



print(dijkstra(0,0))
