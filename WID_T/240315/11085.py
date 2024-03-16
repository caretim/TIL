import sys

input =sys.stdin.readline



n, m= map(int,input().split())


s,e = map(int,input().split())


graph = [[] for __ in range(n)]



for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))


while True:
    flag = 0
    


