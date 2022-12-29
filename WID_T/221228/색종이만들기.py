# https://www.acmicpc.net/problem/2630

import sys

input = sys.stdin.readline

n = int(input())


matrix = [list(map(int, input().split())) for __ in range(n)]

square = [[0] * n for __ in range(n)]

result = [0, 0]
w = 0
b = 0


def s_slice(y, x, j):
    global w, b
    check = matrix[y][x]
    for ny in range(y, y + j):
        for nx in range(x, x + j):
            if matrix[ny][nx] != check:
                s_slice(y, x, j // 2)
                s_slice(y, x + j // 2, j // 2)
                s_slice(y + j // 2, x, j // 2)
                s_slice(y + j // 2, x + j // 2, j // 2)
                return
    if check == 0:
        w += 1
    else:
        b += 1


s_slice(0, 0, n)

print(w)
print(b)
