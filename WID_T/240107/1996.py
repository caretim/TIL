n = int(input())

matrix = [list(input()) for __ in range(n)]

dy, dx = [0, 0, -1, 1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]

result = [[0] * (n) for __ in range(n)]

for y in range(n):
    for x in range(n):
        if matrix[y][x] == ".":
            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and matrix[ny][nx] != ".":
                    result[y][x] += int(matrix[ny][nx])
        else:
            result[y][x] = -1


for i in result:
    for j in i:
        if j >= 10:
            print("M", end="")
        elif j == -1:
            print("*", end="")
        else:
            print(j, end="")
    print("\n", end="")
