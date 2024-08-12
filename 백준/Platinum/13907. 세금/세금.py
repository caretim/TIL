
import sys,heapq

input = sys.stdin.readline

INF = sys.maxsize



n,m,k = map(int,input().split())


graph = [[] for __ in range(n+1)]

s,d = map(int,input().split())


for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

## 왔던 경로 중복으로 도작 방지, 
# 가장 적은 노드방문으로 도착, 
# 한번 탐색할떄, 각 노드의 가중치만큼 더한 횟수로 탐색? 

#k1,2,3을 합한 횟수만큼 한번에 다익돌리기,
#visit리스트를 기준으로 각노드의 값 + 더해주기,

tax = []
for __ in range(k):
    tax.append(int(input()))


#k의 횟수 기준 문제풀이 
#k 완료 리스트 
# comp=[0]*(k+1)
# def dijkstra(start,end):
#     heap =[]
#     for i in range(k+1):
#         heapq.heappush(heap,(0,start,i))
#         visited[i][s]=0
#     while heap:
#         if 0 not in comp:
#             break
#         w,node,v = heapq.heappop(heap)
#         #v번쨰 세금에서 도착지점에 도달한 데이터가 있다면 break
#         if comp[v]:
#             continue
#         if node ==end:
#             comp[v] = w
#             continue
#         for wei,nextnode in graph[node]:
#             nextCost = w+wei+tax[v]
#             if visited[v][nextnode]>nextCost:
#                 visited[v][nextnode]= nextCost

#                 heapq.heappush(heap,(nextCost,nextnode,v))


visited = [[INF for _ in range(n)]for __ in range(n+1)]
#노드 방문 횟수 기준 dijkstra
def dijkstra(start,end):
    heap =[]
    heapq.heappush(heap,(0,start,0)) #비용,노드,방문횟수,
    visited[start][0]=0
    while heap:
        w,node,v = heapq.heappop(heap)
        #적은횟수와 비용으로 이미 노드를 방문했다면 continue
        flag = 0
        for i in range(v+1):
            if visited[node][i]<w:
                flag = 1
                break
        if flag or v ==n-1:
            continue
        for wei,nextnode in graph[node]:
            nextCost = w+wei
            if visited[nextnode][v+1]>nextCost:
                visited[nextnode][v+1]= nextCost
                heapq.heappush(heap,(nextCost,nextnode,v+1))
dijkstra(s,d)


result = INF
for i in range(n):
    if result >visited[d][i]:
        result = visited[d][i]
        max_cnt = i
print(result)

addTax = 0
for k in tax:
    result = INF
    addTax+=k
    for i in range(max_cnt+1):
        if result>visited[d][i]+(i*addTax):
            result = visited[d][i]+(i*addTax)
            
    print(result)

