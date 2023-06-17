import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

site = list(map(int, input().split()))

site[N - 1] = 0  # 마지막 넥서스 0처리

arr = [INF] * (N + 1)

graph = [[] for __ in range(N + 1)]

for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

result = -1
q = []
heapq.heappush(q, (0, 0))
arr[0] = 0
while q:
    w, node = heapq.heappop(q)
    if node == N - 1:
        result = w
        break
    if arr[node] < w:
        continue
    for wei, next_node in graph[node]:
        if site[next_node] != 1:
            cost = w + wei
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))


print(result)
