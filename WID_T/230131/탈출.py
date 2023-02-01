from collections import deque

n,m= map(int,input().split())

matrix= [list(input()) for __ in range(n)]
w_check = [[0]*m for __ in range(n)]
g_check = [[0]*m for __ in range(n)]


dy= [0,0,1,-1]
dx= [1,-1,0,0]

sy,sx=0,0

ey,ex =0,0
warter,end_warter=deque(),deque()
q ,end_q = deque(),deque()
# 티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다.
#  비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

result= "KAKTUS"
find =0

def bfs():
    global result,end_warter,end_q,find
    q = deque(end_q)
    warter =deque(end_warter)
    end_q=deque()
    end_warter=deque()
    while warter:
        y,x = warter.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<= ny <n and 0<=nx<m and w_check[ny][nx]==0:
                if matrix[ny][nx]=='.':
                    w_check[ny][nx]=1
                    matrix[ny][nx]='*'
                    end_warter.append((ny,nx))
    while q:
        y,x,s = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<= ny <n and 0<=nx<m and g_check[ny][nx]==0:
                if matrix[ny][nx]=='D':
                    result=s+1
                    find=1
                    return
                elif matrix[ny][nx]=='.':
                    g_check[ny][nx]=1
                    end_q.append((ny,nx,s+1)) # 흠..시퀀스를 넣어줄까? 안넣어도 될거같긴한데, 전체 카운트를 올릴까 
    if find==1:
        return
    elif len(end_q)>0: # 고슴도치가 이동 할 곳이 없을 경우
        bfs()

for y in range(n):
    for x in range(m):
        if matrix[y][x]=="*":
            end_warter.append((y,x))
        elif matrix[y][x]=="D":
            ey,ex = y,x
        elif matrix[y][x]=="S":
            end_q.append((y,x,0))


bfs()

print(result)






