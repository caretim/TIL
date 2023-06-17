import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize

# 0은 본인 M-1은 최고의원

# 최측근 [1] / 측근 [2] / 비즈니스관계 [3] / 지인 [4]

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    graph = [[] for __ in range(M)]

    for __ in range(N):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    def dijkstra(end):
        arr = [INF] * M
        arr[0] = 0
        q = []
        heapq.heappush(q, (0, 0, [0]))
        while q:
            w, node, node_list = heapq.heappop(q)
            if node == end:
                return node_list
            if arr[node] < w:
                continue
            for wei, next_node in graph[node]:
                cost = w + wei
                if arr[next_node] > cost:
                    arr[next_node] = cost
                    nl = node_list + [next_node]
                    heapq.heappush(q, (cost, next_node, nl))
        return -1

    result = dijkstra(M - 1)
    if result != -1:
        # result = str(result)[1:-1].split(",")
        print(f"Case #{test_case}: ", end="")
        for i in result:
            print(i, end=" ")
        print("")
    else:
        print(f"Case #{test_case}: {result}")
