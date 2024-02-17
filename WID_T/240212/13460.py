#https://www.acmicpc.net/problem/13460
#구슬탈출

import sys
from collections import deque
input =sys.stdin.readline


n,m= map(int,input().split())


matrix = [list(input()) for __ in range(n)]

dy,dx= [0,0,1,-1],[1,-1,0,0]


for y in range(n):
    for x in range(m):
        if matrix[y][x] =='B':
            by,bx= y,x
        elif matrix[y][x]=='R':
            ry,rx= y,x
        elif matrix[y][x]=='O':
            oy,ox = y,x


