# n, m = map(int, input().split())


# matrix = [list(map(int, input().split())) for __ in range(m)]

# dx = [0, 0, 1, -1]
# dy = [-1, 1, 0, 0]

# check = [[0] * n for __ in range(m)]

# result = 0


# while True:
#     ripe = []
#     for y in range(m):
#         for x in range(n):
#             if (matrix[y][x], check[y][x]) == (1, 0):
#                 check[y][x] = 1
#                 for i in range(4):
#                     ny = y + dy[i]
#                     nx = x + dx[i]
#                     if 0 <= ny < m and 0 <= nx < n:
#                         if matrix[ny][nx] == 0:
#                             ripe.append((ny, nx))
#     ripe = set(ripe)
#     if len(ripe) > 0:
#         for y, x in ripe:
#             matrix[y][x] = 1
#         result += 1
#     else:
#         break

# result_sum = 0
# for i in matrix:
#     if i.count(0):
#         result = -1

# print(result)

from collections import deque

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for __ in range(m)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

check = [[0] * n for __ in range(m)]

result = 0

start_list = []
for y in range(m):
    for x in range(n):
        if matrix[y][x] == 1:
            start_list.append((y, x, 0))
            check[y][x] = 1

q = deque(start_list)
while q:
    y, x, c = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n:
            if (matrix[ny][nx], check[ny][nx]) == (0, 0):
                matrix[ny][nx] = 1
                check[ny][nx] = 1
                q.append((ny, nx, c + 1))

for i in matrix:
    if i.count(0):
        c = -1

print(c)
