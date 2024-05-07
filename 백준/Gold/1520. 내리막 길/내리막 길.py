
import sys
input = sys.stdin.readline
import heapq

def bfs():    
    q = [(-maps[0][0], 0, 0)]
    visited[0][0] = 1
    
    while q:
        h, x, y = heapq.heappop(q)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] < maps[x][y]:
                if visited[nx][ny] == 0:
                    heapq.heappush(q, (-maps[nx][ny], nx, ny))
                visited[nx][ny] += visited[x][y]
    return visited[N - 1][M - 1]


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * M for _ in range(N)]
print(bfs())