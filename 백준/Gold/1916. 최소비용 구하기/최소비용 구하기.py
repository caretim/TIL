import heapq 
import sys
input= sys.stdin.readline

INF = sys.maxsize

n=int(input())
m= int(input())

city = [INF]*(n+1)

graph =[[] for __ in range(n+1)]


for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

start,end = map(int,input().split())

def dijkstra(start,end):
    q= []
    heapq.heappush(q,(0,start))
    while q:
        w,node = heapq.heappop(q)
        if city[node]<w:
            continue
        for wei,next_node in graph[node]:
            cost =wei +w 
            if city[next_node]>cost:
                city[next_node]=cost
                heapq.heappush(q,(cost,next_node))
    return city[end]


print(dijkstra(start,end))
