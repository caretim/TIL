from collections import deque

n, m, k, x = map(int, input().split())


city = [[] for __ in range(n + 1)]

visit = [0] * (n + 1)

check = [0] * (n + 1)

result = []


def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1
    while q:
        p = q.popleft()
        for i in city[p]:
            if visit[i] == 0:
                q.append(visit[i])
                visit[i] = 1
                check[i] = 1
                if check[i] == k:
                    result.append(i)


for __ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)


bfs(x)

if len(result) > 0:
    result.sort()
    for r in result:
        print(r)
else:
    print(-1)
