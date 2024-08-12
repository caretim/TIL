import sys

from collections import deque


input = sys.stdin.readline


n= int(input())


graph= [[] for __ in range(n+1) ]

parents= [0] * (n+1)

depth = [0] * (n+1)

visited =[0] * (n+1)

for __ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)

#루트에서 시작해서 각 노드의 뎁스측정
def bfs(start):
    global visited
    que = deque()
    que.append(start)
    visited[start]=1
    # print('실행')
    while que:
        node = que.popleft()
        for nextNode in graph[node]:
            if visited[nextNode] == 0:
                visited[nextNode] = 1
                depth[nextNode]= depth[node]+1
                parents[nextNode]= node
                que.appendleft(nextNode)


# 공통 조상 찾기 알고리즘
def LCA(a,b):
    if depth[a]<depth[b]:
        temp = a
        a= b
        b= temp
    depthCnt = depth[a]-depth[b]
    for __ in range(depthCnt):
        a = parents[a]
    while a!=b:
        a=parents[a]
        b=parents[b]
    print(a)

bfs(1)

m = int(input())

for __ in range(m):
    a,b = map(int,input().split())
    LCA(a,b)