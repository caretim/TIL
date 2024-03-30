import sys
import heapq
from collections import deque

input = sys.stdin.readline

INF = sys.maxsize
# 도시의 수, 길의 수, 좀비에게 점령당한 도시의 수, 위험한 도시의 범위
n,m,k,s = map(int,input().split())


 #일반 도시 p  위험한 도시 q
p,q= map(int,input().split())

graph = [[] for __ in range(n+1)]

infectCity =[] 

flag = [0]*(n+1)

def bfs(infectCity):
    q=deque()
    for i in infectCity:
        flag[i]=-1
        q.append((i,0)) #now,cnt
    while q:
        now,cnt = q.pop()
        if cnt >= s:
            continue
        for next in graph[now]:
            if flag[next]==0:
                flag[next] =1
                q.appendleft((next,cnt+1))
            


visited= [INF]*(n+1)


def dijkstra(start):
    heap =[]
    heapq.heappush(heap,(0,start))
    visited[start]=0
    flag[n] = -2
    while heap:
        cost,now = heapq.heappop(heap)
        if visited[now]<cost:
            continue
        for next in graph[now]: # 감염지역
            if flag[next] == -2:
                return cost
            if flag[next] ==-1:
                continue
            if flag[next]==1: # 위험지역
                nextCost= cost+q

            elif flag[next]==0: # 안전지역
                nextCost = cost+p
        
            if visited[next]>nextCost:
                visited[next]=nextCost
                heapq.heappush(heap,(nextCost,next))



for __ in range(k):
    infectCity.append(int(input()))

for __ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)




bfs(infectCity)

print(dijkstra(1))


# print(visited)    
