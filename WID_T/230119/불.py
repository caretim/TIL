# bfs 탐색으로 나가자 범위 밖으로 나갔을때 탈출

# 벽은 막혀있고 불이 옮겨붙지않는다.

# 다음번에 불이 날 위치까지 불을 미리 넣고 이동 ?

# 1초에 한번씩 탐색해서 진행하게하면 시간초과날거같은데.

# 먼저 불의 위치르 번호를 넣어주고 나서 흠.. 그렇게하면 움직일 떄
# 위치를 어떻게 카운트해서 넣어주지 ?

# while 돌때 한번씩 같이 움직이게해야하나?
# 불먼저 넣어서 시행되도록, 흠 ,,
###.###
# *#.#*#
# 12321#
# 23.2#
# 3.@3.#
#######

from collections import deque

for tc in range(int(input())):
    m, n = map(int, input().split())

    matrix = [list(input()) for __ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    check = 0

    # def escape(start):
    # 초당 반복되도록 구조 변경해주기 @가 주변으로 이동 할 수 없을때,
    # 파이어 큐랑, 이동큐 두개 사용 각각 한번씩 시행 fire큐 먼저 시행 @큐 다음시행

    result = "IMPOSSIBLE"

    # 새 큐가 생겨야하는데? 리스트 두개 번갈아면서 사용하기?
    def fire(start_fire, start):
        global result
        matrix[start[0]][start[1]] = "."
        fire_1 = deque()
        fire_2 = deque()
        user_1 = deque()
        user_2 = deque()
        count = 0
        for y, x in start_fire:
            fire_1.append((y, x))
        user_1.append((start[0], start[1], 0))
        find = 0
        # 리스트 두개를 사용해서 왔다갔다 하도록?
        while True:
            if find == 1 or len(fire_1) + len(fire_2) + len(user_1) + len(user_2) == 0:
                break
            if count % 2 == 0:
                while fire_1:
                    if find == 1:
                        break
                    y, x = fire_1.popleft()
                    for i in range(4):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == ".":
                            matrix[ny][nx] = "*"
                            fire_2.append((ny, nx))
                while user_1:
                    y, x, j = user_1.popleft()
                    for i in range(4):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 > ny or ny >= n or 0 > nx or nx >= m:
                            result = j + 1
                            find = 1
                            break
                        elif 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == ".":
                            user_2.append((ny, nx, j + 1))
            else:
                while fire_2:
                    if find == 1:
                        break
                    y, x = fire_2.popleft()
                    for i in range(4):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == ".":
                            matrix[ny][nx] = "*"
                            fire_1.append((ny, nx))
                while user_2:
                    y, x, j = user_2.popleft()
                    for i in range(4):
                        ny, nx = y + dy[i], x + dx[i]
                        if 0 > ny or ny >= n or 0 > nx or nx >= m:
                            result = j + 1
                            find = 1
                        elif 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == ".":
                            user_1.append((ny, nx, j + 1))
            # print(fire_1, fire_2, user_1, user_2)
            count += 1

    start = 0
    start_fire = []
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == "*":
                start_fire.append((y, x))
            elif matrix[y][x] == "@":
                start = [y, x]

    fire(start_fire, start)

    print(result)
