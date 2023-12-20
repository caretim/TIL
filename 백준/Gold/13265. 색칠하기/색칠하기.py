import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for __ in range(t):
    n, m = map(int, input().split())

    matrix = [[] for __ in range(n + 1)]
    for __ in range(m):
        u, v = map(int, input().split())
        matrix[u].append(v)
        matrix[v].append(u)
    start = u

    visited = [-1] * (n + 1)

    def bfs(start):  # 스타트를 어떻게해줘야하지?
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            now = q.pop()
            for next in matrix[now]:
                if visited[next] == -1:
                    if visited[now] == True:
                        visited[next] = False
                        q.appendleft(next)
                    elif visited[now] == False:
                        visited[next] = True
                        q.appendleft(next)

                elif visited[now] == visited[next]:
                    return "impossible"
        return "possible"

    print(bfs(start))
