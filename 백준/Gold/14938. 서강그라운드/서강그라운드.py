import heapq
import sys

input = sys.stdin.readline


INF = sys.maxsize

N, M, R = map(int, input().split())

items = list(map(int, input().split()))  # 아이템번호 -1해줘야함,
# 각 노드 다익 돌려서 가장 큰 값 확인,

graph = [[] for __ in range(N + 1)]

for __ in range(R):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(start):
    arr = [INF] * (N + 1)
    arr[start] = 0
    q = []
    item_count = 0
    heapq.heappush(q, (0, start))
    while q:
        w, node = heapq.heappop(q)
        if arr[node] < w:
            continue
        for wei, next_node in graph[node]:
            cost = w + wei
            if cost > M:
                continue
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    for i in range(1, len(arr)):
        if arr[i] != INF:
            item_count += items[i - 1]
    return item_count


result = 0

for k in range(1, N + 1):
    r = dijkstra(k)
    if r > result:
        result = r

print(result)
