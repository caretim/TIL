
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
    graph[u].append((v,t,m))
    graph[v].append((u,t,m))


def dijkstra(start, end):
    arr = [[INF for __ in range(10001)] for __ in range(N + 1)]
    arr[1][0] = 0
    q = []
    result = -1
    heapq.heappush(q, (0, 0, start)) # 시간 ,비용 , 노드 
    while q:
        t, m, node = heapq.heappop(q)
        if arr[node][m] < t:
            continue
        for  next_node ,tt, mm, in graph[node]:
            cost = m + mm
            time = t + tt
            if time <= T and cost <= M:
                if arr[next_node][mm] > time :
                    arr[next_node][mm] = time
                    heapq.heappush(q, (time, cost, next_node))
    for i in range(M + 1):
        if arr[end][i] <= T:
            result = i
            break
    return result


print(dijkstra(1, N))
