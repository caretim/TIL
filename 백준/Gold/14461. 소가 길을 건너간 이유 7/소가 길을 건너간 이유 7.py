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