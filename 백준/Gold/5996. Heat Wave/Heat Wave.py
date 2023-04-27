import sys
import heapq

input=sys.stdin.readline
INF = sys.maxsize

N,M,Ts,Te = map(int,input().split())

graph = [[] for __ in range(N+1)]


for __ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))



def dijkstra(start,end):
    arr =[INF] * (N+1)
    arr[start]=0
    q =[]
    heapq.heappush(q,(0,start))
    while q:
        w,n= heapq.heappop(q)
        if arr[n]<w:
            continue
        for wei,next_node in graph[n]:
            cost = w+wei
            if arr[next_node]>cost:
                arr[next_node]=cost
                heapq.heappush(q,(cost,next_node))
    return arr[end]

print(dijkstra(Ts,Te))