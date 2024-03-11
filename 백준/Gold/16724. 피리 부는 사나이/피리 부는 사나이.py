import sys
from collections import deque
input =sys.stdin.readline
move = {
    'U' :[1,0],
    'D' :[-1,0],
    'L' :[0,-1],
    'R' :[0,1]
}
n,m = map(int,input().split())

root= [i for i in range(n*m)]
matrix = [list(input().rstrip()) for __ in range(n)]

visted = [[0]*(m) for __ in range(n)]

result= 0

# def dfs(y,x,circle):
#     global result
#     visted[y][x] =circle
#     dy,dx =move[matrix[y][x]]
#     ny,nx = dy+y ,dx+x
#     if visted[ny][nx] ==0:
#         dfs(ny,nx,circle)
#     elif visted[ny][nx]==circle:
#         result+=1
#         return
#     else:
#         return

# circle = 1
# for y in range(n):
#     for x in range(m):
#         if visted[y][x] == 0:
#             dfs(y,x,circle)
#             circle+=1
# # print(visted)

# print(result)


# 유니온파인드
def find(node):
    if root[node] ==node:
        return node
    else:
        while root[node]!=node:
            node= root[node]
            root[node] = root[root[node]]
        return node

def union(x,y):
    a = find(x)
    b = find(y)
    if a!=b:
        root[b]=root[a]

for i in range(n*m):
    x = i // m
    y = i % m
    nx = 0
    ny = 0
    if matrix[x][y] == "U":
        nx = x -1
        ny = y
    elif matrix[x][y] == "D":
        nx = x + 1
        ny = y
    elif matrix[x][y] == "L":
        nx = x
        ny = y-1
    elif matrix[x][y] == 'R':
        nx = x
        ny = y + 1
    ni = nx*m + ny
    union(i, ni)

visited = dict()
cnt = 0
for i in root:
    p = find(i)
    if p not in visited:
        visited[p] = True
        cnt += 1

print(cnt)