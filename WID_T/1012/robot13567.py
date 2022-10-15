import sys


n, m = map(int, input().split())  # 필드의 크기와 명령어의 갯수를 받는다.

y = 0  # 필드의 최초 시작점은 x는 정상이동좌표 y는 상하반전 위치이므로 y축의 최대값에서 시작한다.
x = 0

turn = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 시작은

tc = 0


# 원래하던대로 돌린다음에 x y만

for __ in range(m):  # 명령어를 입력받음
    command, c = sys.stdin.readline().rstrip().split()
    if command == "TURN":  # turn명령어 들어올때 어디 방향을 바라보고 진행할지 확인한다.
        if c == "0":  # turn 1일시 왼쪽으로 턴
            tc += 1  # 1~4까지 돌 수 있는 위치 확인 최초의 로봇은 오른쪽방향[0,1]을 바라보고있다.
            if tc == 4:  # 4를 넘어간다면 최초의 위치 turn[0]으로 바라보는 방향 지정
                tc = 0
        elif c == "1":  # turn 0일시 오른쪽으로 턴
            tc -= 1  # tc값을 거꾸로 준다.
            if tc == -1:
                tc = 3
    elif command == "MOVE":  # move명령어가 들어온다면 tc턴을 통해 정해진 방향으로 이동한다.
        move = turn[tc]
        ny = y + (move[0] * int(c))  # turn의 위치에 들어있는 튜플의 값을 꺼내서 로봇이 바라 보고있는 방향만큼 이동 .
        nx = x + (move[1] * int(c))
        if 0 > ny or ny > n or 0 > nx or nx > n:  # 범위를 벗어난다면, -1를 프린트 한 후 종료
            print(-1)
            exit(0)
        else:
            y = ny  # 아니라면 이동한 값을 y,x축에 넣어준다.
            x = nx
            print(x, y)
print(x, y)


import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, n = map(int, input().split())
x, y = 0, 0
dir = 0
check = False
for _ in range(n):
    com, num = map(str, input().rstrip().split())

    if com == "TURN":
        if num == "1":
            dir -= 1
            if dir < 0:
                dir = 3
        else:
            dir += 1
            if dir > 3:
                dir = 0
    elif com == "MOVE":
        x += int(num) * dx[dir]
        y += int(num) * dy[dir]
        if x < 0 or x >= M or y < 0 or y >= M:
            print(-1)
            check = True
            break
if ran == 1:
    print(-1)
else:
    print(x, n - y)


import sys


n, m = map(int, input().split())

y = n
x = 0

turn = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ran = 0
tc = 0
for __ in range(m):
    command, c = sys.stdin.readline().rstrip().split()
    if command == "TURN":
        if c == "1":
            tc += 1
            if tc == 4:
                tc = 0
        elif c == "0":
            tc -= 1
            if tc == -1:
                tc = 3
    elif command == "MOVE":
        move = turn[tc]
        ny = y + (move[0] * int(c))
        nx = x + (move[1] * int(c))
        if 0 > ny or ny > n or 0 > nx or nx > n:
            ran = 1
        else:
            y = ny
            x = nx

if ran == 1:
    print(-1)
else:
    print(x, n - y)
