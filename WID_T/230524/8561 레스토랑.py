import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


N, R, M = map(int, input().split())

restaurant = []

for __ in range(R):
    b = int(input())
    restaurant.append(b)

graph = [[] for __ in range(N + 1)]

for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(start):
    arr = [INF] * (N + 1)
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
    for i in range(1, N + 1):
        distance[i] = min(arr[i], distance[i])


distance = [INF] * (N + 1)
for r in restaurant:
    dijk = dijkstra(r)

    # result = max(dijk, result)


print(max(distance[1:]))
