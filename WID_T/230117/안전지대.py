dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [-1, 0, 1, 0, -1, 1, -1, 0, 1]


def solution(board):
    ran = len(board[0])
    print(ran)
    check = [[0] * ran for __ in range(ran)]
    print(check)
    answer = 0
    for y in range(ran):
        for x in range(ran):
            if board[y][x] == 1:
                for i in range(9):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < ran and 0 <= nx < ran:
                        check[ny][nx] = 1
    for y in range(ran):
        for x in range(ran):
            if check[y][x] == 0:
                answer += 1

    return answer


board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

print(solution(board))
