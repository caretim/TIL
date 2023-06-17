import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


N = int(input())
T, M = map(int, input().split())

L = int(input())

graph = [[] for __ in range(N + 1)]

for __ in range(L):
    u, v, t, m = map(int, input().split())
    graph[u].append((m, t, v))
    graph[v].append((m, t, u))


def dijkstra(start, end):
    arr = [[INF] * (N + 10001) for __ in range(N + 1)]
    arr[start] = 0
    q = []
    result = -1
    heapq.heappush(q, (0, 0, start))
    while q:
        m, t, node = heapq.heappop(q)
        t = -t
        if arr[node] < m or t > T:
            continue
        for mm, tt, next_node in graph[node]:
            cost = m + mm
            time = t + tt
            if arr[next_node] > cost and time <= T:
                arr[next_node][mm] = tt
                heapq.heappush(q, (cost, -time, next_node))
    for i in range(M + 1):
        if arr[N][i] <= T:
            result = i
            break
    return result


print(dijkstra(1, N))
