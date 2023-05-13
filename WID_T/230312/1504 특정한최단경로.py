

import heapq 
import sys
input= sys.stdin.readline


INF = sys.maxsize


n,e = map(int,input().split())



graph =[[] for __ in range(n+1)]

for __ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

check_node = list(map(int,input().split()))



# 흠,,최단거리 체크를 3개를 더 넣어서 확인하기? 
# 체크노드를 들렀다 간다하면 흠 ,, 1번에서 체크포인트 각각 도착한 후 다음 노드로 출발, 
def dijkstra(start,end):
    arr = [INF]*(n+1)
    arr[start]=0
    arr[0]=-1
    q= []
    heapq.heappush(q,(0,start))
    while q:
        w,node = heapq.heappop(q)
        # if (node,check1,check2) == (end,1,1):
        #     result = w
        #     break
        
        if arr[node]<w: 
            continue
        for wei,next_node in graph[node]: # 마지막노드일때는 check,1,2가 1,1이여야함,, 
            # if next_node == n:
            #         if check1 ==0 or check2 ==0:
            #             continue
            cost = w+wei
            if arr[next_node]>cost:
                arr[next_node] = cost
                # if next_node == check_node[0]:
                #     check1 =1
                # if next_node == check_node[1]:
                #     check2 =1 
                heapq.heappush(q,(cost,next_node))
    # if arr[end] == INF:
    #     return 
    # else:
    return arr[end] 

r = []


p1 = dijkstra(1,check_node[0])+dijkstra(check_node[0],check_node[1])+dijkstra(check_node[1],n)
p2 = dijkstra(1,check_node[1])+dijkstra(check_node[1],check_node[0])+dijkstra(check_node[0],n)


if p1 < INF : # 바운더리 테케 확인 설정 
    r.append(p1)
if p2 < INF:
    r.append(p2)

if len(r)>0:
    print(min(r))
else:
    print(-1)                            



