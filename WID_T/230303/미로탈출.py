maps = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]

from collections import deque
import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = 0


def solution(maps):

    before_matrix = [list(m) for m in maps]

    h = len(maps)
    w = len(maps[0])
    for y in range(h):
        for x in range(w):
            if before_matrix[y][x] == "S":  # 시작지점 -1
                before_matrix[y][x] = 0
                start_point = [y, x]
            elif before_matrix[y][x] == "E":
                before_matrix[y][x] = 0
                end_point = [y, x]
            elif before_matrix[y][x] == "O":  # 통로 0
                before_matrix[y][x] = 0
            elif before_matrix[y][x] == "X":  # 벽 1
                before_matrix[y][x] = 1
            elif before_matrix[y][x] == "L":  # 레버 2
                before_matrix[y][x] = 2
                lp = [y, x]

    after_map = copy.deepcopy(before_matrix)
    after_map[lp[0]][lp[1]] = 0
    after_map[end_point[0]][end_point[1]] = 3  # 레버찾은 후 탈출구 찾기위해 배열값변경

    def search(matrix, y, x, j):
        global answer
        # check =[[0]*len(maps[0]) for __ in range(maps)]
        print("탐색중")
        q = deque()
        matrix[y][x] = 1
        q.append((y, x, j + 1))
        while q:
            y, x, j = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < h and 0 <= nx < w:
                    if matrix[ny][nx] == 2:
                        search(after_map, ny, nx, j)
                        return
                    elif matrix[ny][nx] == 3:
                        answer = j
                        return
                    elif matrix[ny][nx] == 0:
                        matrix[ny][nx] = 1
                        q.append((ny, nx, j + 1))

    search(before_matrix, start_point[0], start_point[1], 0)

    if answer == 0:
        result = -1
    else:
        result = answer
    return result


print(solution(maps))
