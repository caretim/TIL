import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

INF = sys.maxsize

distance = [INF] * (V + 1)

graph = [[] for __ in range(V + 1)]

heap = []
start = int(input())


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        wei, node = heapq.heappop(heap)

        if distance[node] < wei:
            continue

        for w, next_node in graph[node]:
            next_wei = wei + w

            if next_wei < distance[next_node]:
                distance[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))


for __ in range(E):
    u, v, w = map(int, input().split())  # 출발노드u  도착노드 v  가중치 w
    graph[u].append((w, v))  # 그래프에 (가중치,도착노드) 튜플로 추가

dijkstra(start)

for i in range(1, V + 1):
    print("INF" if distance[i] == INF else distance[i])
