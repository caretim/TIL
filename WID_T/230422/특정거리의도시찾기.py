import sys
import heapq

INF = sys.maxsize

N, M, K, X = map(int, input().split())


arr = [INF] * (N + 1)

graph = [[] for __ in range(N + 1)]


for __ in range(M):
    node, wei = map(int, input().split())
    graph[node].append(wei)


def dijkstra(n, k):
    result = []
    q = []
    arr[n] = 0
    heapq.heappush(q, (0, n))
    while q:
        w, node = heapq.heappop(q)
        if arr[node] < w:
            continue
        for next_node in graph[node]:
            cost = w + 1
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    for i in range(1, len(arr)):
        if arr[i] == k:
            result.append(i)

    return result


r = dijkstra(X, K)

if len(r) == 0:
    print(-1)
else:
    for i in r:
        print(i)
