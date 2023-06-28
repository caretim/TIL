import sys
import heapq


INF = sys.maxsize
input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[INF]*(N) for __ in range(N)]



for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))