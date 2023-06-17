import sys
import heapq


INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(start, end):
    arr = [INF] * (N + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, node = heapq.heappop(q)
        if arr[node] < w:
            continue
        if node == end:
            return arr[end]
        for wei, next_node in graph[node]:
            cost = w + wei
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return arr[end]


N, M = map(int, input().split())

graph = [[] for __ in range(N + 1)]

node_list = []

for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))
    # heapq.heappush(node_list, (w, u, v))


s, t = map(int, input().split())


# for i in range(len(node_list)):
#     w, u, v = heapq.heappop(node_list)
#     graph[u].append((w, v))
#     graph[v].append((w, u))
#     dijk = dijkstra(s, t)
#     if dijk != INF:
#         print(dijk)
#         break


dijk = dijkstra(s, t)

print(dijk)
