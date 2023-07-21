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

#방문지 체크, 0,1로 해주고, 거울 횟수는 직접가져가기
def dijkstra(sy,sx,ey,ex):
    check[sy][sx]=0
    q=[]
    

    


