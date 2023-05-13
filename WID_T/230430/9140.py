import heapq
import sys

input = sys.stdin.readline


def dijkstra(s, c):
    arr = [INF] * (N + 1)
    arr[s] = 0
    q = []
    heapq.heappush(q, (0, S))
    while q:
        w, n = heapq.heappop(q)
        if arr[n] < w:
            continue
        for wei, next_node in graph[n]:
            cost = wei + w
            if arr[next_node] > cost:
                heapq.heappush(q, (cost, next_node))
                arr[next_node] = cost
    return arr[c]


while True:
    N, M, S, C = map(int, input().split())

    if (N, M, S, C) == (0, 0, 0, 0):
        break

    INF = sys.maxsize

    graph = [[] for __ in range(N + 1)]

    for __ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[u].append((w, v))

    print(dijkstra(S, C))
