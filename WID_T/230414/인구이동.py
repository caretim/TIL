N, L, R = map(int, input().split())

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

matrix = [list(map(int, input().split())) for __ in range(N)]


def bfs(y, x):
    change_day = 0
