#https://www.acmicpc.net/problem/2176

import sys
import heapq
from collections import deque

input =sys.stdin.readline

INF = sys.maxsize

n,m= map(int,input().split())

graph = [[] for __ in range(n)]

dp = [0]*n

arr = [INF]*n

for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u-1].append((w,v-1))
    graph[v-1].append((w,u-1))


#마지막 지점에서 각 노드로 이동하며 순서 노드 가중치 부여하기
#그리고 다시 시작점에서 진행하며 각 노드 순서 가중치가 적은 순으로 이동,
#1.도착지점에서 각 노드 이동 후 각 지점 이동거리 측정,
#2.1번 노드 거리에서 거리가 더 짧은 노드로 이동시 옳은경로, 아닐시 x 
#3.set을 사용해서 사용되는 경로 중복안되게만들기,

def check_wei():
    heap = []
    heapq.heappush(heap,(0,1))
    arr[1]=0
    while heap:
        cost,node = heapq.heappop(heap)
        if arr[node]<cost:
            continue
        for wei,nextNode in graph[node]:
            nextcost = cost+wei
            if arr[nextNode]>nextcost:
                arr[nextNode]=nextcost
                heapq.heappush(heap,(nextcost,nextNode)) 
            if cost > arr[nextNode]:
                dp[node]+=dp[nextNode]

# def check_path():
#     stack = []
#     stack.append((arr[0],0))
#     cnt = 0
#     while stack:
#         cost,node = stack.pop()
#         for wei,nextNode in graph[node]:
#             if nextNode==1:
#                 cnt+=1
#                 continue
#             if arr[nextNode]<arr[node]:
#                 stack.append((arr[nextNode],nextNode))
#     return cnt
    
dp[1]=1
    
check_wei()

print(dp[0])




        
        