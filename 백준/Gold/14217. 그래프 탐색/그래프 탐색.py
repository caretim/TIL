import sys
from collections import deque

input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())

city = [set() for __ in range(n + 1)]

for __ in range(m):
    u, v = map(int, input().split())
    city[u].add(v)
    city[v].add(u)


q = int(input())


def move():
    q = deque()
    q.append((1))
    visited = [-1] * (n + 1)
    visited[1] = 0
    while q:
        now = q.pop()
        for i in city[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.appendleft((i))
    return visited[1:]


for __ in range(q):
    g, u, v = map(int, input().split())
    if g == True:
        city[u].add(v)
        city[v].add(u)
    else:
        city[u].remove(v)
        city[v].remove(u)
    print(*move())
