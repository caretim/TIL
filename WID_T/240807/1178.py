import sys
from collections import deque
input = sys.stdin.readline

#시작되는 노드는 연결간선이 최소인 노드 ,
#노드에 간선이 아예 존재하지 않는다면 +1 



n,m = map(int,input().split())


graph=[[] for __ in range(n+1)]

paths = []

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append((v,i))
    graph[v].append((u,i))
    paths.append(1)



visited= [0]*(n+1)
visited[0]=1
def dfs(start):
    visited[start]=0
    que = deque()
    que.append(start)
    while que:
        now = que.popleft()
        for next,pathNum in graph[now]:
            if paths[pathNum]==1:
                paths[pathNum]=0
                visited[next]=1
                que.appendleft(next)


for i in range(m):
    if visited[i]==0:
        dfs(i)

print(sum(paths))

            
