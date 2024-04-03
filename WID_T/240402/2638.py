import sys
import copy 
n,m= map(int,input().split())

matrix =[list(map(int,input().split())) for __ in range(n)]


visited = [[0]*(m) for __ in range(n)]

dy,dx =[0,0,1,-1],[1,-1,0,0]


cheese = []

for y in range(n):
    for x in range(m):
        if matrix[y][x]:
            cheese.append((y,x))
# 공기가 접촉되어있는 곳 카운트하기,
# 바깥 공기 2로 바꿔주기

            
def find_air(visited,y,x):
    if visited[y][x]  or matrix[y][x]:
        return
    visited[y][x] = 1
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        if 0<=ny<n and 0<=nx<m:
            find_air(visited,ny,nx)


find_air(visited,0,0)

result= 0
def bfs(visited,cheese):
    next_visited =copy.deepcopy(visited)
    next_cheese = []
    while cheese:
        y,x = cheese.pop()
        air = 0
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx]==1:
                    air +=1
        if air>1:
            matrix[y][x] =0
            find_air(next_visited,y,x)
        else:
            next_cheese.append((y,x))
    return next_visited,next_cheese


while cheese:
    result+=1
    visited,cheese= bfs(visited,cheese)




print(result)
