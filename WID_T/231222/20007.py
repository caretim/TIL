import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

n, m, x, y = map(int, input().split())

graph = [[] for __ in range(n)]

for __ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

visited = [INF for __ in range(n)]

visited[y] = 0

heap = []

heapq.heappush(heap, (0, y))

while heap:
    w, now = heapq.heappop(heap)
    if visited[now] < w:
        continue
    for wei, next in graph[now]:
        next_wei = w + wei
        if visited[next] > next_wei:
            visited[next] = next_wei
            heapq.heappush(heap, (next_wei, next))

visited.sort()


if visited[-1] * 2 > x:
    print(-1)
else:
    day = 1
    distance = 0
    for i in range(n):
        if x >= distance + visited[i] * 2:
            distance += visited[i] * 2
        else:
            day += 1
            distance = visited[i] * 2
    print(day)
