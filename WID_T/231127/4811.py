import sys

input = sys.stdin.readline

r, c = map(int, input().split())

matrix = []


def vex(y, x):
    num_list = []
    for yy in range(y, y + 3):
        for xx in range(x, x + 3):
            num_list.append(matrix[yy][xx])
    num_list.sort()
    if num_list[4] >= t:
        return True


for __ in range(r):
    matrix.append(list(map(int, input().split())))

t = int(input())


cnt = 0
for y in range(r - 2):
    for x in range(c - 2):
        if vex(y, x):
            cnt += 1

print(cnt)


# print(matrix)
