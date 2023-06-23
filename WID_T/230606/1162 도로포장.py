import sys
import heapq


INF = sys.maxsize
input = sys.stdin.readline

N,M,K = map(int, input().split())

graph = [[] for __ in range(N + 1)]



for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

arr =  [[INF for _ in range(K+1)] for _ in range(N+1)] 

def dijkstra(start):
    arr[start][0] = 0
    q = []
    heapq.heappush(q, (0, start,0))

    while q:
        w, city,cnt = heapq.heappop(q)
        if arr[city][cnt] < w:
            continue
        for wei, next_city in graph[city]:
            cost = w + wei
            if arr[next_city][cnt] > cost:
                arr[next_city][cnt] = cost
                heapq.heappush(q, (cost, next_city,cnt))

            if cnt < K:
                if arr[next_city][cnt+1] > w: # 넘어가는 비용으로 0으로 만들어 기존의 코스트를 넘겨준다,
                    arr[next_city][cnt+1]=w
                    heapq.heappush(q,(w,next_city,cnt+1))



dijkstra(1)

print(min(arr[N]))
