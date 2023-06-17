import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

for tc in range(int(input().rstrip())):

    # 도시의수,총비용,티켓정보의 수
    N, M, K = map(int, input().split())

    graph = [[] for __ in range(N + 1)]

    # 인천은 언제나 1번 도시이고, LA는 언제나 N번 도시이다
    for __ in range(K):
        u, v, c, d = map(int, input().split())  #
        graph[u].append((v, c, d))
        # 소요시간,비용,도착노드
    status = [[INF] * (M + 1) for _ in range(N + 1)]
    status[1][0] = 0
    for money in range(M + 1):
        for vertex in range(1, N + 1):
            if status[vertex][money] != INF:
                for v, c, d in graph[vertex]:
                    if money + c <= M:
                        status[v][money + c] = min(
                            status[v][money + c], status[vertex][money] + d
                        )
    result = min(status[N])
    if result == INF:
        print("Poor KCM")
    else:
        print(result)

    # def dijkstra(start):
    #     visit = [INF] * (N + 1)
    #     visit[start] = 0
    #     q = []
    #     heapq.heappush(q, (0, 0, start))
    #     result = "Poor KCM"
    #     while q:
    #         d, c, node = heapq.heappop(q)
    #         c = -c
    #         if visit[node] < d or c > M:
    #             continue
    #         if node == N:
    #             return dist
    #         for nd, nc, next_node in graph[node]:
    #             dist = d + nd
    #             cost = c + nc
    #             if cost > 10:
    #                 continue
    #             if dist < visit[next_node]:
    #                 visit[next_node] = dist
    #                 heapq.heappush(q, (dist, -cost, next_node))
    #     return result

    # # 반례, 당장 노드에 도착해서 늦을 수도 있지만,
    # # 늦은 경유지를 통해서 다음공항에서는 더 빠르게 도착 할 수도 있다?

    # # 비용만 체크하고 나머지는
    # print(dijkstra(1))
