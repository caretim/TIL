from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    q = deque([])
    q.append(start)
    visit = [0] * (n + 1)
    visit[start] = 1
    while q:
        num = q.popleft()
        for i in adj[num]:
            if not visit[i]:
                visit[i] = visit[num] + 1
                q.append(i)

    for v in range(1, n + 1):
        visit[v] -= 1

    return sum(visit)


n, m = map(int, input().split())
lst = []

for _ in range(m):
    lst.extend(list(map(int, sys.stdin.readline().split())))

adj = [[] for _ in range(n + 1)]
for i in range(m):
    n1, n2 = lst[i * 2], lst[i * 2 + 1]
    adj[n1].append(n2)
    adj[n2].append(n1)

answer = []
for i in range(1, n + 1):
    answer.append(bfs(i))

print(answer.index(min(answer)) + 1)
