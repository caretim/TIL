import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


# 농장,시간,소,경로
F,P,C,M =map(int,input().split())



graph = [[] for __ in range(F + 1)]

for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))




