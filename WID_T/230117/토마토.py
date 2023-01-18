n, m = map(int, input().split())


matrix = [list(map(int, input().split())) for __ in range(m)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

check = [[0] * n for __ in range(m)]

result = 0


while True:
    ripe = []
    result += 1
    for y in range(m):
        for x in range(n):
            if (matrix[y][x], check[y][x]) == (1, 0):
                print("토마토발견")
                check[y][x] = 1
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < m and 0 <= nx < n:
                        if matrix[ny][nx] == 0:
                            ripe.append((ny, nx))
                            print("토마토담기")
    ripe = set(ripe)
    print(ripe)
    if len(ripe) > 0:
        for y, x in ripe:
            matrix[y][x] = 1
    else:
        break

print(result)
