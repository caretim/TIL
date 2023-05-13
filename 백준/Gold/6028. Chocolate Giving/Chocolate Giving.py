import sys
import heapq


INF = sys.maxsize
input = sys.stdin.readline




def dijsdtra(start):
    arr =[INF] *(N+1)
    arr[start] =0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        w,node = heapq.heappop(q)
        if arr[node] <w:
            continue
        for wei , next_node in graph[node]:
            cost = w+wei
            if arr[next_node]>cost:
                arr[next_node] =cost
                heapq.heappush(q,(cost,next_node))
    return arr


N,M,B = map(int,input().split())


graph = [[] for __ in range(N+1)]



for __ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))


result = dijsdtra(1)

for __ in range(B):
    A,B = map(int,input().split())
    print(result[A]+result[B])