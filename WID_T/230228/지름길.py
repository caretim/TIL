

import heapq


n,d = map(int,input().split())

graph = [[] for __ in range(d+1)] # 각 거리 리스트 지정

INF=int(1e9)
distance =[INF] * (d+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dis ,now =heapq.heappop(q)
        if dis<distance[now]:
            continue
        for i in graph[now]:
            cost = dis+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,1[0]))



for i in range(d):
    graph[i].append((i+1,1))

for __ in range(n):
    s,e,g=map(int,input().split())
    graph[s].append((e,g))

dijkstra(0)
print(distance[d])

