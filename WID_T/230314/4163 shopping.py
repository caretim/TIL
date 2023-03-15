import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize


c, p, pb, pa1, pa2 = map(int, input().split())

graph = [[] for __ in range(c)]

for __ in range(c):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(start, end):
    dist = [INF] * (p + 1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, node = heapq.heappop(q)
        if node == end:
            return dist[node]
        if dist[node] < w:
            continue
        for wei, next_node in graph[node]:
            cost = w + wei
            if dist[next_node] > cost:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))


pass1 = dijkstra(pb, pa1) + dijkstra(pa1, pa2)
pass2 = dijkstra(pb, pa2) + dijkstra(pa2, pa1)

print(min(pass1, pass2))
