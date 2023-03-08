from collections import deque

import sys

input = sys.stdin.readline
n= int(input())
k= int(input())

# 0,0시작?

# 큐에 꼬리의 길이 넣어놓기,
matrix=[[0]*n for __ in range(n)]

move = [(0,1),(1,0),(0,-1),(-1,0)]

d = 0 # 0,1,2,3 으로 방향움직임, L =-1 D = +1  음수 -> 3   4일시 ->0 

for __ in range(k):
    y,x, = map(int,input().split())
    matrix[y-1][x-1] = 2

command = {}

for __ in range(int(input())):
    c,cc = input().split()
    c= int(c)
    if c not in command:
        command[c]=cc

def snake(y,x):
    global d
    q= deque()
    q.append((y,x))
    matrix[y][x] =1
    count=0
    while True:
        if count in command:
            if command[count] == 'L':
                d-=1
            elif command[count] =='D':
                d+=1
            if d<0:
                d=3
            elif d>3:
                d=0
        count+=1 # 위치 바뀌기전에 카운터 올라가면 안됨,
        ny,nx = y+move[d][0] , x+move[d][1]
        if 0<=ny<n and 0<=nx<n:
            if matrix[ny][nx]==1: # 꼬리 마주쳤을때 
                return count
            elif matrix[ny][nx]==0: # 빈공간 
                matrix[ny][nx]=1
                q.append((ny,nx))
                yy,xx= q.popleft()
                matrix[yy][xx]=0
            elif matrix[ny][nx]==2: # 사과주웟을때 
                matrix[ny][nx]=1
                q.append((ny,nx))
            y,x =ny,nx
            
        else:
            return count






print(snake(0,0))



