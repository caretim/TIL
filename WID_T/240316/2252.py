

import sys
from collections  import deque

input=sys.stdin.readline
n,m=map(int,input().split())

count = [0]*(n)
graph = [[] for __ in range(n)]

for __ in range(m):
    u,v = map(int,input().split())
    u-=1;v-=1
    graph[u].append(v)
    count[v]+=1


q= deque()
for i in range(n):
    if count[i] ==0:
        q.append(i)

result = []

while q:
    now= q.popleft()
    if count[now] ==0:
        result.append(now+1)
        count[now]-=1
    for next in graph[now]:
        if count[next]>0:
            count[next]-=1
            q.appendleft(next)


print(*result)