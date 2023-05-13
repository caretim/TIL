import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize


n, m = map(int, input().split())


graph = [[] for __ in range(n + 1)]

for __ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


x, y, z = map(int, input().split())

# 출발 정점 X에서 출발하여 중간 정점 Y를 거쳐서 도착 정점 Z에 도달하는 최단 거리
# 출발 정점 X에서 출발하여 중간 정점 Y를 거치지 않고 도착 정점 Z에 도달하는 최단 거리
# 도착 할 수 없다면 -1


def dijkstra(start, end, check):
    arr = [INF] * (n + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, node = heapq.heappop(q)
        if arr[node] < w:
            continue
        for wei, next_node in graph[node]:
            cost = w + wei
            if check == False and next_node == y:
                continue
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return arr[end]


r1 = dijkstra(x, y, 1) + dijkstra(y, z, 1)

r2 = dijkstra(x, z, 0)

print(r1 if r1 < INF else -1, r2 if r2 < INF else -1)
