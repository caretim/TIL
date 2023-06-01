import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[] for __ in range(N + 1)]


for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def dijkstra(start):
    visit = [[] for _ in range(N + 1)]  # 우선순위 q로 들어오기에 들어오는 순서대로 방문타입라인찍기,
    q = []
    heapq.heappush(visit[start], 0)  # 비용
    heapq.heappush(q, (0, start))  # 비용, 장소
    while q:
        w, node = heapq.heappop(q)
        for wei, next_node in graph[node]:
            cost = w + wei
            if len(visit[next_node]) < K:
                heapq.heappush(visit[next_node], -cost)
                # 최대힙으로 사용,
                heapq.heappush(q, (cost, next_node))
            elif cost < -visit[next_node][0]:  # 코스트가 다음노드의 제일 큰값보다 작다면, 갱신
                heapq.heappop(visit[next_node])
                heapq.heappush(visit[next_node], -cost)
                heapq.heappush(q, (cost, next_node))
    for i in range(1, N + 1):  # 각노드를 확인며 k번째 최단경로(cost)가 존재한다면 값 넣기, 아니라면 -1
        if len(visit[i]) == K:
            print(-visit[i][0])
        else:
            print(-1)


dijkstra(1)
