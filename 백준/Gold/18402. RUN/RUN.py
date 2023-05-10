import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize


N = int(input())
escape_room = int(input())

time = int(input())


M = int(input())

graph = [[] for __ in range(N + 1)]

rooms = [INF] * (N + 1)
for __ in range(M):
    u, v, w = map(int, input().split())
    graph[v].append((w, u))


def dijkstra(end):
    rooms[end] = 0
    q = []
    result = 0
    heapq.heappush(q, (0, end))
    while q:
        w, room = heapq.heappop(q)
        if rooms[end] < w:
            continue
        for t, next_room in graph[room]:
            cost_time = w + t
            if rooms[next_room] > cost_time:
                rooms[next_room] = cost_time
                heapq.heappush(q, (cost_time, next_room))
    for r in rooms:
        if 0 <= r <= time:
            result += 1
    return result


print(dijkstra(escape_room))

