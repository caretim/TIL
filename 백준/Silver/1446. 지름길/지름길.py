

import heapq
import sys

n,d = map(int,input().split())

graph = [[] for __ in range(10001)] # 각 거리 리스트 지정

INF=sys.maxsize

distance =[INF] *(10001)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dis ,now =heapq.heappop(q)
        if dis>distance[now]:
            continue
        for w,next_node in graph[now]:
            wei = dis+w
            if wei < distance[next_node]:
                distance[next_node] = wei
                heapq.heappush(q,(wei,next_node))


for i in range(d+1): 
    graph[i].append((1,i+1)) # 가중치,노드 기본값 지정  i+1,1

for __ in range(n):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))


dijkstra(0)
print(distance[d])

