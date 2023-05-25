import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


# 각 교차로 도착시 물의양 추가,
N, M, P = map(int, input().split())


graph = [[] for __ in range(N + 1)]

for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(start, end):
    arr = [INF] * (N + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, city = heapq.heappop(q)
        if arr[city] < w:
            continue
        if city == end:
            return int(w)
        for wei, next_city in graph[city]:
            cost = w + wei
            if arr[next_city] > cost:
                arr[next_city] = cost
                heapq.heappush(q, (cost, next_city))
    print(arr)


a = dijkstra(1, N)
b = dijkstra(1, P)
c = dijkstra(P, N)


if a == b + c:
    print("SAVE HIM")
else:
    print("GOOD BYE")
