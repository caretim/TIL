import sys

input = sys.stdin.readline


matrix = [list(map(int, input().split())) for __ in range(9)]


my, mx = 0, 0

max = -1


for y in range(9):
    for x in range(9):
        if matrix[y][x] > max:
            max = matrix[y][x]
            my = y
            mx = x


print(max)
print(my + 1, mx + 1)
