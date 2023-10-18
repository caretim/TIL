import heapq

import sys

input = sys.stdin.readline

INF = sys.maxsize

n,m,Q,k =map(int,input().split())



secret =list(map(int,input().split()))

graph =[[] for __ in range(n)]

result = [INF for __ in range(n)]

for __ in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)


def bfs(secret,k):
    visit = [INF for __ in range(n)]
    q = []
    day= 0
    flag = 0
    for i in secret:
        i-=1
        q.append((i,k))
        visit[i]=0
    while flag < n-Q:
        day+= 1
        next_q =[]
        while q:
            node,kd = q.pop()
            if kd <= 0:
                continue
            for next_node in graph[node]:
                if visit[next_node]==INF:
                    flag+=1
                    visit[next_node]=day
                    next_q.append((next_node,k*(day+1)))
                    q.append((next_node,kd-1))
                elif visit[next_node]>day:
                    q.append((next_node,kd-1))
        q=next_q
    return visit


print(*bfs(secret,k))
        


    



