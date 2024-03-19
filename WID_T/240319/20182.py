import sys

import heapq
input = sys.stdin.readline

INF =sys.maxsize

n,m,a,b,c, =map(int,input().split())

graph= [[] for __ in range(n)]


for __ in range(m):
    u,v,w= map(int,input().split())
    u-=1;v-=1
    graph[u].append((w,v))
    graph[v].append((w,u))


visited = [INF]*n
emote= [INF]*n

def dijkstra(start):
    heap = []
    heapq.heappush(heap,(0,start,0))
    visited[0]=0
    emote[0]=0
    while heap:
    