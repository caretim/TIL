from collections import deque
import sys


input = sys.stdin.readline

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

r, c = map(int, input().split())


matrix = [list(input().rstrip()) for __ in range(r)]


def bfs(y, x):
    q = set()
    q.add((0, 0, matrix[y][x]))
    result = 0
    while q:
        y, x, checker = q.pop()
        result = max(result, len(checker))
        if result == 26:
            return 26
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and matrix[ny][nx] not in checker:
                q.add((ny, nx, checker + matrix[ny][nx]))
    return result


print(bfs(0, 0))
