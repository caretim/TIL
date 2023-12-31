import sys

input = sys.stdin.readline
r1, c1, r2, c2 = map(int, input().split())


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

x, y = 0, 0  # 시작점
size = (c2 - c1 + 1) * (r2 - r1 + 1)

length = 1
dir = 0
num = 1
count_max_num = 0
while size > 0:
    # 같은 length 2번 반복 후, length + 1
    for i in range(2):
        for j in range(length):
            if r1 <= x <= r2 and c1 <= y <= c2:
                board[x - r1][y - c1] = num
                count_max_num = num
                size -= 1
            x += dx[dir]
            y += dy[dir]
            num += 1

        dir = (dir + 1) % 4  # 방향
    length += 1

blank = len(str(count_max_num))

for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(board[i][j]).rjust(blank), end=" ")
    print()
