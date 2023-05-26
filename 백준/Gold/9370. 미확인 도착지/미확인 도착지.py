import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


def dijkstra(start):
    arr = [INF] * (n + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, node = heapq.heappop(q)
        if arr[node] < w:
            continue
        for wei, next_node in graph[node]:
            cost = w + wei
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return arr


# def dijkstra(start, end):
#     arr = [INF] * (n + 1)
#     arr[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))
#     while q:
#         w, node = heapq.heappop(q)
#         if node == end:
#             return w
#         if arr[node] < w:
#             continue
#         for wei, next_node in graph[node]:
#             cost = w + wei
#             if arr[next_node] > cost:
#                 arr[next_node] = cost
#                 heapq.heappush(q, (cost, next_node))


for tc in range(int(input())):

    n, m, t = map(int, input().split())

    s, g, h = map(int, input().split())

    graph = [[] for __ in range(n + 1)]

    # g,h를 거쳐서 갈 수 있는 노드 , 그 중에서 최소거리,

    # s -> g,h 가는시간 , g,h에서 출발하여 후보지에 도착하는 거리

    # 우회하지않는다,
    # 최단거리로만 이동하기에, 최단거리가 아니면 후보지에서 제외,

    # 모든 최단거리 한번 구하고,
    # s->g->h+후보 거리와 # s->h->g+후보 거리
    # 두개 돌려서 최단거리와 동일하다면 , result에 추가하기,

    for __ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    candcity = []

    for __ in range(t):
        c = int(input())
        candcity.append(c)

    # 찾을때 최단거리로 먼저 도착하는곳?
    # 양방향임,, g,h를 무조건 거쳐야함, 그렇다면
    # g,h중 어디로 먼저 도착해서 지나가는가,

    result = []
    dis_s = dijkstra(s)
    dis_g = dijkstra(g)
    dis_h = dijkstra(h)
    for i in candcity:
        # 최단거리[g] + g에서 i 목적지 + h에서 g까지 이동거리,
        if (
            dis_s[g] + dis_g[h] + dis_h[i] == dis_s[i]
            or dis_s[h] + dis_h[g] + dis_g[i] == dis_s[i]
        ):
            result.append(i)
    result.sort()
    print(*result, end=" ")
