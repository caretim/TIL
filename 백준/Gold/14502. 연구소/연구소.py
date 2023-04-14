import sys
from itertools import combinations
import copy

input = sys.stdin.readline


n, m = map(int, input().split())

born_matrix = [list(map(int, input().split())) for __ in range(n)]

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
wall_list = []
start_list = []


def dfs(wall):
    stack = copy.deepcopy(start_list)
    matrix = copy.deepcopy(born_matrix)
    count = 0
    for y, x in wall:
        matrix[y][x] = 1
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = 2
                    stack.append((ny, nx))

    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 0:
                count += 1

    return count, matrix


for y in range(n):
    for x in range(m):
        if born_matrix[y][x] == 0:
            wall_list.append((y, x))
        elif born_matrix[y][x] == 2:
            start_list.append((y, x))


wall_list = combinations(wall_list, 3)

result = 0
for wall in wall_list:
    count, l = dfs(wall)
    if result < count:
        result = count
        # for a in l:
        #     print(a)
print(result)
