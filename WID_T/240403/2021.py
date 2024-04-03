import sys

import heapq

INF = sys.maxsize

n,m= map(int,input().split())

station = [[] for __ in range(n+1)]
train = []


visited = [INF]*(n+1)



for i in range(m):
    TL = list(map(int,input().split()))
    train.append(TL[:-1])
    for t in range(len(TL)-1):
        station[TL[t]].append(i)


start,end = map(int,input().split())


def dijkstra(start):
    visited[start] =0
    heap= []
    heapq.heappush(heap,((0,start)))
    
    while heap:
        cnt,now =heapq.heappop(heap)
        if visited[now] 