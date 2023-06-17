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
        if w > C: # 비용이 초과되면 정지, 
            continue
        for wei, next_node in graph[node]: 
            cost = w + wei 
            if cost > C or visit[node][next_node]: #비용 합이 초과되거나, 같은경로를 통해서 왔을때, 최소힙으로 오기에 최대값중 작은 값이 먼저체크됨,
                continue
            elif next_node == B:  # 도착지에 왔다면, 최대값 비교, 
                result = min(result, max(max_v, wei))
            visit[node][next_node] = True # 전경로를 통해 온 곳은 방문체크
            heapq.heappush(q, (max(max_v, wei), next_node, cost))
    return result


dijk = dijkstra(A, B, C)

if dijk == INF:
    print(-1)
else:
    print(dijk)

# 전단계 