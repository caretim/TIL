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

# def dijkstra(mid):
#     heap = []
#     heapq.heappush(heap,(0,start,0))
#     visited[0]=0
#     emote[0]=0
#     while heap:
        
    
# import heapq
# import sys
 
# input=sys.stdin.readline
 
# n,m,a,b,c=map(int,input().split())
# INF=int(1e14)+1
# graph=[[] for _ in range(n)]
 
# def dijkstra(mid):
#     pq=[]
#     cost=[INF]*(n+1)
#     heapq.heappush(pq,(0,a))
#     cost[a] = 0
#     while pq:
#         cos,cur=heapq.heappop(pq)
#         if cost[cur] != cos:
#             continue
#         for i in graph[cur]:
#             nxt,cst=i
#             if cst>mid:
#                 continue
#             if cost[nxt]>cost[cur]+cst :
#                 cost[nxt]=cost[cur]+cst
#                 if nxt==b and cost[nxt]<=c:
#                     return True
#                 heapq.heappush(pq,(cost[nxt],nxt))
#     return cost[b]<=c
 
# # 0 index로 하기위해서
# a-=1
# b-=1
# costs = []
# for i in range(m):
#     s,e,d=map(int,input().split())
#     s-=1
#     e-=1
#     graph[s].append((e,d))
#     graph[e].append((s,d))
#     heapq.heappush(costs,-d)
 
# costs = sorted(costs)
# L=0
# R=-heapq.heappop(costs)
# ans=INF
# while L<=R:
#     mid=(L+R)//2
#     if dijkstra(mid):
#         ans=min(ans,mid)
#         R=mid-1
#     else:
#         L=mid+1
 
# if ans==INF:
#     print(-1)
# else:
#     print(ans)