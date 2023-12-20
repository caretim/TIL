from collections import deque

import sys

input = sys.stdin.readline

INF = sys.maxsize

n, m, Q, k = map(int, input().split())


secret = list(map(int, input().split()))

graph = [[] for __ in range(n)]

result = [INF for __ in range(n)]

for __ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def bfs(secret, k):
    visit = [INF for __ in range(n)]
    q = deque()
    for i in secret:
        i -= 1
        q.append((i, k, 1))
        visit[i] = 0
    while q:
        node, kd, day = q.pop()
        kd -= 1
        for next_node in graph[node]:
            if visit[next_node] > day:
                visit[next_node] = day
                if kd > 0:  # kd가 1이상 남았을때,
                    q.appendleft((next_node, kd, day))
                elif kd == 0:  # kd를 모두 소모해서 0일때
                    q.appendleft((next_node, k * (day + 1), day + 1))

    return visit


print(*bfs(secret, k))
