import sys
import heapq


INF = sys.maxsize
input = sys.stdin.readline

N,M = map(int, input().split())

graph = [[INF]*(N) for __ in range(N)]



for i in range(M):
    u, v, w = map(int, input().split())
    graph[u-1].append((w, v-1))
    graph[v-1].append((w, u-1))


def floyd()