import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

N, M = map(int, input().split())

arr = [INF] * (N + 1)

graph = [[] for __ in range(N + 1)]

for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(finish):
    q = []
    heapq.heappush(q, (0, 1))
    arr[1] = 0
    while q:
        w, node = heapq.heappop(q)
        if w > arr[node]:
            continue
        for wei, next_node in graph[node]:
            cost = wei + w
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return


dijkstra(N)

# print(arr)
# for i in graph:
#     print(i)
print(arr[N])
