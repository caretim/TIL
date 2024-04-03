import sys
import heapq
input =sys.stdin.readline

INF = sys.maxsize

move = {
    '/' : [(-1,1),(1,-1)],

    '\\': [(1,1),(-1,-1)]

}

n,m =map(int,input().split())


matrix = [list(input()) for __ in range(n)]

visited = [[INF] * m for __ in range(n)]


