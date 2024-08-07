import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline

n,m= map(int,input().split())

graph = [[] for __ in range(n+1)]

for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))


s,h= map(int,input().split())

house_list = list(map(int,input().split()))
store_list = list(map(int,input().split()))



def dijkstra(store_list):
    arr=[INF]*(n+1)
    q= []
    for i in store_list:
        arr[i]=0
        heapq.heappush(q,(0,i))
    while q:
        w,node=heapq.heappop(q)
        if arr[node]<w:
            continue
        for wei,next_node in graph[node]:
            cost = w+wei
            if arr[next_node]>cost:
                arr[next_node]=cost
                heapq.heappush(q,(cost,next_node))
    return arr


r = dijkstra(store_list)

result = []

min_dist= INF

for i in house_list:
    if r[i]<min_dist:
        min_dist=r[i]
        result=[]
        result.append(i)
    elif r[i]==min_dist:
        result.append(i)

result.sort()
print(result[0])

