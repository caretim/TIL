import sys

input = sys.stdin.readline


INF = sys.maxsize

n, m = map(int, input().split())

graph = []

distance = [INF] * (n + 1)

for __ in range(m):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))


def bellman_ford(start):
    distance[start] = 0
    for i in range(1, n + 1):
        # 각 노드의 간선 확인
        for j in range(m):
            now = graph[j][0]
            next_node = graph[j][1]
            node_cost = graph[j][2]
            if distance[now] != INF and distance[next_node] > node_cost + distance[now]:
                distance[next_node] = node_cost + distance[now]
                if i == n:
                    return True
    return False


negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])


# import sys
# input = sys.stdin.readline
# INF = int(1e9)


# def bellman_ford(start):
#     dist[start] = 0

#     # n번의 라운드를 반복
#     for i in range(1, n + 1):
#         # 매 라운드마다 모든 간선을 확인
#         for j in range(m):
#             now, next, cost = edges[j][0], edges[j][1], edges[j][2]
#             # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if dist[now] != INF and dist[next] > dist[now] + cost:
#                 dist[next] = dist[now] + cost
#                 # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
#                 if i == n:
#                     return True

#     return False


# n, m = map(int, input().split())
# edges = []
# dist = [INF] * (n + 1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     edges.append((a, b, c))

# negative_cycle = bellman_ford(1)

# if negative_cycle:
#     print(-1)
# else:
#     for i in range(2, n + 1):
#         # 도달할 수 없는 경우
#         if dist[i] == INF:
#             print(-1)
#         # 도달 가능한 경우
#         else:
#             print(dist[i])
