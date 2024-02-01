import sys
import heapq

input =sys.stdin.readline

# 연결된 건물이 모두 완성되어야 현재 건물 건설 가능

# 직전노드에서 가장 오래걸렸던 시간 + 본인시간

n,k = map(int,input().split())

arr = list(map(int,input().split()))

node_time = [[]]

graph = [[] for __ in range(n)]


for __ in range(k):
    x,y = map(int,input().split())
    graph[y-1].append(x-1)


target = int(input()) -1