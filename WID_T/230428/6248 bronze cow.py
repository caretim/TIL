import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())

graph = [[] for __ in range(N + 1)]


for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(end):
    arr = [INF] * (N + 1)
    arr[end] = 0
    q = []
    heapq.heappush(q, (0, end))
    while q:
        w, n = heapq.heappop(q)
        if arr[n] < w:
            continue
        for wei, next_node in graph[n]:
            cost = wei + w
            if arr[next_node] > cost:
                heapq.heappush(q, (cost, next_node))
                arr[next_node] = cost
    return arr


distance = dijkstra(X)

for i in range(len(distance)):
    if distance[i] == INF:
        distance[i] = 0

print((max(distance) * 2))
