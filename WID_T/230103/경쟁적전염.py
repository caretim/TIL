import sys
from collections import deque


input= sys.stdin.readline


n,k = map(int,input().split())


matrix = [list(map(int,input().split())) for __ in range(n)]

time,fy,fx= map(int,input().split())

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def contagious(fy,fx,time,arr):
    arr = deque(arr)
    for __ in range(time):
        for __ in range(len(arr)):
            k= arr.popleft()
              # 힙을 사용해서 중간에 1로 추가되는 좌표가 계속 반복됨, 순차적으로 빼야한다, 힙말고 덱사용
            for i in range(4):
                ny,nx = k[1]+dy[i],k[2]+dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if matrix[ny][nx]==0:
                        matrix[ny][nx]=k[0]
                        arr.append((k[0],ny,nx))
    return(matrix[fy-1][fx-1])
arr=[]

for y in range(n):
    for x in range(n):
        if matrix[y][x]!=0:
           arr.append((matrix[y][x],y,x))
arr.sort()
arr=deque(arr)


print(contagious(fy,fx,time,arr))

