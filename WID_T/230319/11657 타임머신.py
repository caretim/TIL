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
    for i in range(n):
        # 각 노드의 간선 확인
        for j in range(m):
            old_node = graph[j][0]
            next_node = graph[j][1]
            node_cost = graph[j][2]
            if (
                distance[old_node] != INF
                and distance[next_node] > node_cost + distance[old_node]
            ):
                distance[next_node] = node_cost + distance[old_node]
                if i == n - 1:
                    return True
    return False


negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)

else:
    for i in range(2, v + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
