import sys
from collections import deque

# 횟수와 이동거리 중 최단거리가 우선, 횟수 이내로 움직이는 범위를 어떻게?
# 시작 = 1,1 끝 = n,m 각각 -1씩 해줘야함,
# z축 확인해주기,
input = sys.stdin.readline


dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n, m, k = map(int, input().split())

matrix = [list(map(int, input().rstrip())) for __ in range(n)]


check = [[[0] * m for __ in range(n)] for __ in range(k)]


def bfs(y, x):
    result = -1
    q = deque()
    q.append((y, x, 0, 0))
    check[0][y][x] = 1
    while q:
        y, x, z, count = q.popleft()
        print(y, x, z)
        if (y, x) == (n - 1, m - 1):
            return count, z
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if (matrix[ny][nx], check[z][ny][nx]) == (0, 0):  # 일반 길일떄 ,
                    check[z][ny][nx] = 1  # 매트릭스 0 z축위치,
                    q.append((ny, nx, z, count + 1))
                elif (
                    matrix[ny][nx] == 1 and z + 1 < k
                ):  # 부수고 온 벽을? 또? count로 확인하자, # 매트릭스에서 벽일때, z축 k범위를 넘지 않는다면
                    if check[z + 1][ny][nx] < count:  # 벽을 만났을때 벽을 부순위치에서 탐색,
                        print("시행되나?")  # 갔던 곳을 다시 안가게하려면 ??
                        check[z + 1][ny][nx] = count + 1
                        q.append((ny, nx, z + 1, count + 1))
    return result


print(matrix, "원본")
for j in check:
    print(j)


print(bfs(0, 0))
