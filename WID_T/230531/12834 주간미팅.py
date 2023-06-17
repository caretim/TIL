import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

N,V,E = map(int,input().split())

A,B =map(int,input().split())

TM = list(map(int,input().split()))



graph = [[] for __ in range(V + 1)]

for __ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(start,end):
    arr = [INF] * (V + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, city = heapq.heappop(q)
        if arr[city] < w:
            continue
        for wei, next_city in graph[city]:
            cost = w + wei
            if arr[next_city] > cost:
                arr[next_city] = cost
                heapq.heappush(q, (cost, next_city))
    if arr[end] == INF:
        return -1
    else:
        return arr[end]

result= 0

for m in TM:
    result+= dijkstra(m,A) + dijkstra(m,B)

print(result)