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
