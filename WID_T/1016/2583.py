from collections import deque


m, n, k = map(int, input().split())


matrix = [[0] * (n) for __ in range(m)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


result = []


# m = 5세로 n=7 가로
def bfs(y, x):
    size = 1
    matrix[y][x] = 1
    q = deque()
    q.append((y, x))
    print(q)
    while q:
        k = q.popleft()
        for i in range(4):
            ny = k[0] + dy[i]
            nx = k[1] + dx[i]
            if 0 <= ny < m and 0 <= nx < n:
                if matrix[ny][nx] == 0:
                    q.append((ny, nx))
                    matrix[ny][nx] = 1
                    size += 1
    return size


for __ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            matrix[y][x] = 1

for y in range(m):
    for x in range(n):
        if matrix[y][x] == 0:
            result.append(bfs(y, x))

result.sort()

print(len(result))
# for r in result:
#     print(r, end=" ")

print(" ".join(map(str, result)))
