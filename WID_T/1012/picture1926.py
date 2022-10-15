n, m = map(int, input().split())


matrix = [list(map(int, input().split())) for __ in range(n)]

# 4방위 델타탐색
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
size = []  # 그림의 크기 저장
#


def dfs(y, x):
    check_size = 1  # 최초의 그림 한조각
    matrix[y][x] = 0
    stack = [(y, x)]
    while stack:
        k = stack.pop()
        for i in range(4):
            ny = dy[i] + k[0]
            nx = dx[i] + k[1]
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == 1:
                    check_size += 1  # 찾을때마다 그림 조각 추가
                    matrix[ny][nx] = 0
                    stack.append((ny, nx))
    return check_size  # 찾은 그림의 크기


for y in range(n):
    for x in range(m):
        if matrix[y][x] == 1:
            size.append(dfs(y, x))  # dfs를 통해 찾은 그림의 크기를 size리스트에 넣어줌

print(len(size))  # 누적된 그림의 갯수 출력
if len(size) == 0:  # 만일 그림이 0개라면 0출력
    print("0")
else:
    print(max(size))  # 아니라면 제일 큰 그림 출력
