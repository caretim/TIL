
from collections import deque


            
def solution(maps):
    answer = []
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    new_map = [list(l) for l in maps]
    maps = new_map
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if new_map[y][x]=='X':
                new_map[y][x]=0
            else:
                new_map[y][x] = int(new_map[y][x])


    def bfs(y,x,j):
        days = j
        q = deque()
        q.append((y,x))
        maps[y][x]=0
        while q:
            y,x = q.popleft()
            for i in range(4):
                ny,nx= y+dy[i],x+dx[i]
                if 0<=ny<len(maps) and 0<= nx<len(maps[0]):
                    if maps[ny][nx]!=0:
                        days+= maps[ny][nx] 
                        maps[ny][nx]=0
                        q.append((ny,nx))
        return days

    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] != 0:
                find = bfs(y,x,maps[y][x])
                if find>0:
                    answer.append(find)

    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer