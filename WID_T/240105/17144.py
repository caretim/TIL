import sys

input = sys.stdin.readline


dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]

r, c, t = map(int, input().split())


matrix = [list(map(int, input().split())) for __ in range(r)]

q = []

ac = []

for y in range(r):
    for x in range(c):
        if matrix[y][x] > 0:
            q.append((y, x))
        elif matrix[y][x] < 0:
            ac.append((y, x))


def dust(q):
    # matrix[y][x]-(matrix[y][x]//5)*4  if matrix[y][x] >0: next_q.append()
    new_matrix = [[0] * (c) for __ in range(r)]
    next_q = set()
    while q:
        y, x = q.pop()
        if matrix[y][x] < 4:
            new_matrix[y][x] = 0
            continue

        extend = (matrix[y][x] // 5) * 4
        new_matrix[y][x] = matrix[y][x] - extend * 4

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                new_matrix[ny][nx] += extend
                next_q.add((ny, nx))
    q = list(next_q)
    matrix = new_matrix


def clean(ac):
    
