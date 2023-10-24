import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


matrix = [list(map(int, input().split())) for __ in range(n)]


visit = [[0] * m for __ in range(n)]


cnt = 0
cheese = 0
q = deque()
q.append((1, 0))
visit[1][0] = 1
flag = 1
while flag:
    next_q = deque()
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0:
                if matrix[ny][nx] == 0:
                    visit[ny][nx] = 1
                    q.appendleft((ny, nx))
                else:
                    visit[ny][nx] = 1
                    next_q.append((ny, nx))
    if len(next_q) == 0:
        flag = 0
    else:
        cheese = len(next_q)
        cnt += 1
        q = next_q

print(cnt)
print(cheese)


# for mx in matrix:
#     print(mx)


# print(11111)
# for vi in visit:
#     print(vi)
