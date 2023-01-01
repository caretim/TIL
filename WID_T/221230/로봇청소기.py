import sys

input = sys.stdin.readline

n, m = map(int, input().split())

now_y, now_x, now_d = map(int, input().split())

# 북 0 동 1  남 2 서 3
# 1.현재 위치를 청소한다.
# 2.현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.

home = [list(input().split()) for __ in range(n)]

check = [[0] * m for __ in range(n)]

going = [0, 1, 2, 3]

move = [[1, 0], [0, -1], [-1, 0], [0, 1]]


cnt = 1


def clean(y, x, d):
    global cnt
    check[y][x] = 1
    home[y + move[d][0]][x + [move[d][1]]]
    return


print(clean(now_y, now_x, now_d))
