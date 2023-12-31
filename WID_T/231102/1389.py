from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for __ in range(n)]


for __ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    q = deque([])
    q.append(start)
    visit = [0] * (n)
    visit[start] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visit[next] == 0:
                visit[next] = visit[now] + 1
                q.append(next)
    return sum(visit) - 1


result = 0
min = sys.maxsize

for i in range(n):
    cnt = bfs(i)
    if cnt < min:
        min = cnt
        result = i
    # result.append(bfs(i))


print(result + 1)
