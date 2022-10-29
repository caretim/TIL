from collections import deque

n,m=map(int,input().split())

dy = [0,0,-1,1]
dx = [-1,1,0,0]

matrix= [list(input()) for __ in range(n)]

check_list = [[0]*m for __ in range(n)]


def dfs(y,x):
    cnt = 1
    q= deque()
    q.append((y,x,cnt))
    check_list[y][x] = cnt
    while q:
        k =  q.popleft()
        for i  in range(4):
            ny = k[0] + dy[i] 
            nx = k[1] + dx[i]
            cnt = k[2] +1
            if 0 <= ny < n and 0 <= nx < m :
               if matrix [ny][nx] == '1' and check_list[ny][nx] == 0:
                q.append((ny,nx,cnt))
                check_list[ny][nx] = cnt
    return (check_list[n-1][m-1])


print(dfs(0,0))

# for y in range(n):
#     for x in range(m):
#        if  matrix[y][x] == 1: 






