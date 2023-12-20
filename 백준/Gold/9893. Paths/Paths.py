import sys, heapq

input = sys.stdin.readline


INF = sys.maxsize
# 최단경로 우선, 이후 같은 길이의 경로중 가중치가 적은것,

n, m = map(int, input().split())

graph = [[] for __ in range(n)]


for __ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def dijkstra(start, end):
    heap = []
    visited = [(INF, INF) for __ in range(n)]
    visited[start] = (0, 0)
    heapq.heappush(heap, (0, 0, 0))  # 거리,가중치,노드
    while heap:
        dis, wei, node = heapq.heappop(heap)
        if visited[node][0] < dis:
            continue
        elif visited[node][0] == dis and visited[node][1] < wei:
            continue
        next_dis = dis + 1
        for w, next_node in graph[node]:
            next_wei = w + wei
            if visited[next_node][0] > next_dis:
                visited[next_node] = (next_dis, next_wei)
                heapq.heappush(heap, (next_dis, next_wei, next_node))
            elif visited[next_node][0] == next_dis and visited[next_node][1] > next_wei:
                visited[next_node] = (next_dis, next_wei)
                heapq.heappush(heap, (next_dis, next_wei, next_node))
    return visited[end]


x, w = dijkstra(0, 1)

print(w)
