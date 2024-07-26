import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


n,m =map(int,input().split())


oilCost =list(map(int,input().split()))

## 다음노드로 이동할떄, 최초비용계산,
#노드 분기 - 최초 비용 ,현재비용으로 마지막까지 사용, 실시간 비용 갱신

# 각 노드를 들를떄 3^n의 시간

# 노드 방문시 사용비용 비교 

# 현재 노드의 기름 구매 비용 <-> 이동간 거리의 사용비용 

# 더 적은 비용으로 노드에 도착할 경우 and  현재노드 가격보다 낮은 가격으로 이동중일 경우

graph= [[] for __ in range(n+1)]
visited = [[INF for __ in range(max(oilCost)+1)] for __ in range(n+1)]

for __ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

#비용은 고정비, 각 노드에 고정 비용체크리스트?  -> 사용중인 기름이 현재 기름보다 높다면 갱신, 낮다면 그대로,
def dijkstra(start):
    visited[start][oilCost[start-1]]=0
    heap =[]
    heapq.heappush(heap,(0,start,oilCost[start-1])) # 비용, 노드 , 사용 기름 가격
    while heap:
        cost,node,oil = heapq.heappop(heap)
        if node == n:
            print(cost)
            break
        oil = min(oil,oilCost[node-1])
        if visited[node][oil]<cost:
            continue
        for dist,nextNode in graph[node]:
            nextCost = cost + dist*oil
            # if min(visited[nextNode][0:oil])<nextCost:
            #     continue
            if visited[nextNode][oil]>nextCost:
                visited[nextNode][oil]=nextCost
                heapq.heappush(heap,(nextCost,nextNode,oil))
        #  다음 이동 거리 경로에 따른 오일 가격 기대치, 
        # 사용 오일이 더 낮은 경우, 

dijkstra(1)
# print(min(visited[n]))
            

    
