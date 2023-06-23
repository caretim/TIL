import heapq
import sys

input = sys.stdin.readline

INF =sys.maxsize




w,h = map(int,input().split())

graph=[[]for __ in range(h)]

check=[[-1]*(w) for __ in range(h)]

for i in range(h):
    graph[i] = list(input())

c_list= []

for y in range(h):
    for x in range(w):
        if graph[y][x]=='c':
            c_list.append((y,x))


def dijkstra(sy,sx,ey,ex):
    q=[]
    

    


