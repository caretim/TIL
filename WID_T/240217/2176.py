#https://www.acmicpc.net/problem/2176

import sys
import heapq
from collections import deque

input =sys.stdin.readline

INF = sys.maxsize

n,m= map(int,input().split())

graph = [[] for __ in range(n)]

Node_weigh = [-1]*n

arr = [INF]*n

for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))


#마지막 지점에서 각 노드로 이동하며 순서 노드 가중치 부여하기
#그리고 다시 시작점에서 진행하며 각 노드 순서 가중치가 적은 순으로 이동,
#1.각 노드의 위치에서 도착지점까지의 길이는 모두 다르다.
#1-1.노드의 길이 
q = deque()
q.append((0,0))
while q:
    node,cnt = q.pop()
    for cnt,nextNode in graph[node]:
        if Node_weigh[nextNode]==-1:
            Node_weigh[nextNode]=cnt+1
            q.appendleft((node,cnt+1))


heap = heapq()
heapq.heappush((heap,(0,1,0)))
while heap:
    cost,node,cnt = heapq.heappop(heap)
    for wei,nextNode in graph[node]:
        nextcost = cost+wei
        
        