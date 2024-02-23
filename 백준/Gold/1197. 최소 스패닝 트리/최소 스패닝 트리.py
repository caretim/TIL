import sys
import heapq
input =sys.stdin.readline


n,m = map(int,input().split())


graph = [[] for __ in range(n)]




for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u-1].append((w,v-1))
    graph[v-1].append((w,u-1))


def prim(graph):
    total =0
    heap =graph[0]
    heapq.heapify(heap)
    check =set()
    check.add(0)
    while heap:
        cost,node = heapq.heappop(heap)
        if node not in check:
            check.add(node)
            total+=cost
            for nextCost,nextNode in graph[node]:
                if nextNode not in check:
                    heapq.heappush(heap,(nextCost,nextNode))
    return total

print(prim(graph))
