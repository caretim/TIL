import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for __ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 범위 벗어났을때 반전 범위로 탐색하게 만들기
def dfs(y, x):
    stack = []
    stack.append((y, x))
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 > ny or 0 > nx or n <= ny or m <= nx:
                if ny < 0:
                    ny = n - 1
                elif ny >= n:
                    ny = 0
                elif nx < 0:
                    nx = m - 1
                elif nx >= m:
                    nx = 0
            if matrix[ny][nx] == 0:
                stack.append((ny, nx))
                matrix[ny][nx] = 1


# 넘어갔을 경우 y축일때  위로 올라가게되면 y-1  내려가게되면 y 0
# 오른쪽도 마찬가지로 오른쪽넘어가면0 왼쪽 넘어가면 x-1

result = 0

for y in range(n):
    for x in range(m):
        if matrix[y][x] == 0:
            dfs(y, x)
            result += 1

print(result)
