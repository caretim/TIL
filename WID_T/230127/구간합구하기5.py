import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for __ in range(n)]


def sum_range(x1, y1, x2, y2):
    result = 0
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            result += matrix[y][x]
    return result


for case in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_range(x1 - 1, y1 - 1, x2 - 1, y2 - 1))
