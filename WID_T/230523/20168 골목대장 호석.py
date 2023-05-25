# 개수 N, 골목 개수 M, 시작 교차로 번호 A, 도착 교차로 번호 B, 가진 돈 C
import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline


N, M, A, B, C = map(int, input().split())


graph = [[] for __ in range(N + 1)]


for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def dijkstra(A, B, C):
    visit = [[False] * (N + 1) for __ in range(N + 1)]
    q = []
    heapq.heappush(q, (0, A, 0))
    result = INF
    while q:
        max_v, node, w = heapq.heappop(q)
        if w > C:
            continue
        for wei, next_node in graph[node]:
            cost = w + wei
            if cost > C or visit[node][next_node]:  # 이동경로가 전 단계를 밟아왔을때,
                continue
            elif next_node == B:
                result = min(result, max(max_v, wei))
            visit[node][next_node] = True
            heapq.heappush(q, (max(max_v, wei), next_node, cost))
    return result


dijk = dijkstra(A, B, C)

if dijk == INF:
    print(-1)
else:
    print(dijk)
