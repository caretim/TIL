from collections import deque


for __ in range(int(input())):
    n = int(input())

    start_y, start_x = map(int, input().split())

    end_y, end_x = map(int, input().split())

    area = [[0] * n for __ in range(n)]

    dy = [2, 1, 2, 1, -2, -1, -2, -1]
    dx = [1, 2, -1, -2, 1, 2, -1, -2]

    def bfs(y, x):
        q = deque()
        q.append((y, x, 0))
        while q:
            y, x, r = q.popleft()
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if (ny, nx) == (end_y, end_x):
                    print(r + 1)
                    q = deque()
                    break
                if 0 <= ny < n and 0 <= nx < n:
                    if area[ny][nx] == 0:
                        area[ny][nx] = 1
                        q.append((ny, nx, r + 1))

    if (start_y, start_x) == (end_y, end_x):
        print(0)
    else:
        bfs(start_y, start_x)
### 마지막케이스
