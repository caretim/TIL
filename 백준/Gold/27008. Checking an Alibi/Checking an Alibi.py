import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


# 필드,경로,소,시간
F,P,C,M =map(int,input().split())
# 필드 1 는 헛간,


graph = [[] for __ in range(F + 1)]

for __ in range(P):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))



yd = [[] for __ in range(F+1)]

for i in range(C):
    fd = int(input())
    yd[fd].append(i+1)


def dijkstra(start):
    arr =[INF]*(F+1)
    arr[start]= 0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        wei,node = heapq.heappop(q)
        if arr[node]<wei:
            continue
        for next_wei,next_node in graph[node]:
            cost = wei+next_wei
            if arr[next_node]>cost:
                arr[next_node]=cost
                heapq.heappush(q,(cost,next_node))
    return arr



r = dijkstra(1)



result = []
for i in range(1,F+1):
    if r[i] <= M:
        result= result+yd[i]


result.sort()
print(len(result))
print(*result,sep="\n")

