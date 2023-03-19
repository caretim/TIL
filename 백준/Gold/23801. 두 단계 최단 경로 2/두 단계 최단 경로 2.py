import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for __ in range(n + 1)]

for __ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

x, z = map(int, input().split())

p = int(input())

mn = list((map(int, input().split())))


def dijkstra(start):
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
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return arr


arr1 = dijkstra(x)

arr2 = dijkstra(z)

result = INF
for i in mn:
    if result > arr1[i] + arr2[i]:
        result = arr1[i] + arr2[i]


print(result if INF > result else -1)
