import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

n= int(input())
m= int(input())

city = [INF]*(n+1)


graph = [[] for __ in range(n+1)]

def dijkstra(start,end):
    q=[]
    heapq.heappush(q,(0,start,1,[start]))
    city[start]=0
    while q:
        wei,node,c,l = heapq.heappop(q)
        if node == end:
            return city[node],c,l
        if wei > city[node]:
            continue
        for w,next_node in graph[node]:
            new_list = list(l)
            if wei+w < city[next_node]:
                city[next_node]= wei+w
                new_list.append(next_node)
                heapq.heappush(q,(w+wei,next_node,c+1,new_list))
    





for __ in range(m):
    u,v,w, = map(int,input().split())
    graph[u].append((w,v))

start,end = map(int,input().split())

sc,ec,l = dijkstra(start,end)
print(sc)
print(ec)
print(*l)