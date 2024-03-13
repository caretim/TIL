import sys
from collections import deque
input =sys.stdin.readline


dy,dx=  [0,0,1,-1],[1,-1,0,0]
r,c = map(int,input().split())


matrix = [list(input().rstrip()) for __ in range(r)]




