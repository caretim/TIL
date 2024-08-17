import sys,heapq


input = sys.stdin.readline


n= int(input())


graph= [[] for __ in range(n+1) ]



for __ in range(n-1):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))


# def dijkstra()

m = map(int,input())

for __ in range(m):
    dij
