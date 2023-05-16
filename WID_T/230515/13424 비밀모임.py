import sys
import heapq


INF = sys.maxsize
input = sys.stdin.readline

for tc in range(int(input())):
    N, M = map(int, input().split())

    result = [0] * (N)

    graph = [[] for __ in range(N + 1)]

    for __ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    man = int(input())
    members = list(map(int, input().split()))

    def dijkstra(start):
        arr = [INF] * (N + 1)
        arr[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            w, node = heapq.heappop(q)
            if arr[node] < w:
                continue
            for wei, next_node in graph[node]:
                cost = w + wei
                if arr[next_node] > cost:
                    arr[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
        for i in range(1, len(arr)):
            result[i - 1] = result[i - 1] + arr[i]

    for m in members:
        dijkstra(m)

    tmp = min(result)
    index = result.index(tmp)
    print(index + 1)
