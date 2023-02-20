from collections import deque

s, t = map(int, input().split())
check = set()
INF = 10**9


def bfs(s, t):
    global check
    q = deque()
    q.append((s, ""))
    while q:
        n, r = q.popleft()
        if n == t:
            return r

        aft = n * n
        if 0 < aft <= INF and aft not in check:
            check.add(aft)
            q.append((aft, r + "*"))
        aft = n + n
        if 0 < aft <= INF and aft not in check:
            check.add(aft)
            q.append((aft, r + "+"))
        aft = n / n
        if 0 < aft <= INF and aft not in check:
            check.add(aft)
            q.append((aft, r + "/"))
    return -1


if s == t:
    print(0)
else:
    print(bfs(s, t))
