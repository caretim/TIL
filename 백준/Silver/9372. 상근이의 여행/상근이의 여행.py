

from collections import deque

import sys

input= sys.stdin.readline
case= int(input())

for __ in range(case):
    n,m=map(int,input().split())

    graph = [[] for __ in range(n+1)]

    for i in range(m):
        u,v =map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    visit = [0] *(n+1)
    q= deque() 
    q.append(u)
    visit[u]=1
    cnt=0
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visit[i]==0:
                visit[i]=1
                q.append(i)
                cnt+=1

    print(cnt)        
