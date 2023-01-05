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

home = [list(map(int,input().split())) for __ in range(n)]

check = [[0] * m for __ in range(n)]


move = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북 동 남 서 #  4로 남을 때 반시계방향으로 진행 가능 1 증가할때마다 왼쪽으로

cnt = 1

def clean(y, x, d):
    global cnt
    check[y][x] = 1
    while True:
        suc=0
        for i in range(4):# d부터 순차적으로 올라가야함, 반시계방향으로 진행 어떻게 방향을 확인시키지? 현재위치에서 왼쪽
            d= (d+3)%4
            ny = y+move[d][0]
            nx = x+move[d][1]
            if 0 <= ny < n and 0 <= nx < m :
                if home[ny][nx] == 0  and  check[ny][nx] == 0:
                    cnt+=1
                    check[ny][nx]=1
                    y=ny
                    x=nx
                    suc=1
                    break
        # 뒤로 간 후 방향체크 뒤로는 어떻게? 현재 좌표에서, 바라보고있는 좌표의 값을 빼주면됨 [1,0],[1,1],[1,2]일때, 
             #가운데에서 왼쪽을 볼때 뒤로가면 x+1  반대로는 x-1 값을 거꾸로주니 기존좌표를 빼주면 된다., 
        if suc ==0:
            # print(y-move[d][0],x-move[d][1])
            if home[y-move[d][0]][x-move[d][1]] == 1 : # 벽이 존재할때만, 청소한 곳은 체크안해도됨 벽일 경우에만 중지 
                break
            else:
                y = y-move[d][0]
                x = x-move[d][1]
    return cnt

print(clean(now_y, now_x, now_d))

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

home = [list(map(int,input().split())) for __ in range(n)]

check = [[0] * m for __ in range(n)]


move = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북 동 남 서 #  4로 남을 때 반시계방향으로 진행 가능 1 증가할때마다 왼쪽으로

cnt = 1

def clean(y, x, d):
    global cnt
    check[y][x] = 1
    while True:
        suc=0
        for i in range(4):# d부터 순차적으로 올라가야함, 반시계방향으로 진행 어떻게 방향을 확인시키지? 현재위치에서 왼쪽
            d= (d+3)%4
            ny = y+move[d][0]
            nx = x+move[d][1]
            if 0 <= ny < n and 0 <= nx < m :
                if home[ny][nx] == 0  and  check[ny][nx] == 0:
                    cnt+=1
                    check[ny][nx]=1
                    y=ny
                    x=nx
                    suc=1
                    break
        # 뒤로 간 후 방향체크 뒤로는 어떻게? 현재 좌표에서, 바라보고있는 좌표의 값을 빼주면됨 [1,0],[1,1],[1,2]일때, 
             #가운데에서 왼쪽을 볼때 뒤로가면 x+1  반대로는 x-1 값을 거꾸로주니 기존좌표를 빼주면 된다., 
        if suc ==0:
            if home[y-move[d][0]][x-move[d][1]] == 1 : # 벽이 존재할때만, 청소한 곳은 체크안해도됨 벽일 경우에만 중지 
                break
            else:
                y = y-move[d][0]
                x = x-move[d][1]
    return cnt

print(clean(now_y, now_x, now_d))

