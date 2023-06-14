import sys 
import heapq
import copy

input = sys.stdin.readline

INF =sys.maxsize

while True:

    N,M= map(int,input().split())

    if (N,M) ==(0,0):
        break
    S,D = map(int,input().split())

    graph = [[] for __ in range(N)]

    for i in range(M):
        u,v,w = map(int,input().split())
        graph[u].append((w,v,i))

    road = [0]*(M+1)

    def first_dijkstra(s,d):
        node_check=[]
        road_check =[[] for __ in range(N+1)]
        arr=[INF]*(N+1)
        q=[]
        arr[s]=0

        heapq.heappush(q,(0,s,list()))
        while q:
            w,node,rl =heapq.heappop(q)
            if arr[node]<w:
                continue
            for wei,next_node,i in graph[node]:
                cost = w+ wei
                if next_node == d: # 경로 도착시, 최단경록로 도착한 도로기록을 기록,
                    if arr[next_node]>cost:
                        arr[next_node]=cost
                        node_check = rl+[next_node]
                        road_check[next_node]=[i]
                        #지나온 도로 기록,
                    elif arr[next_node]==cost:
                        node_check=node_check+rl+[next_node]
                        road_check[next_node]= road_check[next_node] + [i]

                else: 
                    if arr[next_node]>cost: # 경로확인을 위해 같을 경우에도 힙추가,
                        arr[next_node]=cost
                        rll= rl+[next_node] #노드 도착 기록 
                        road_check[next_node]=[i] #노드에 최소값도착시, 도로 갱신
                        heapq.heappush(q,(cost,next_node,rll))

                    elif arr[next_node]==cost: # 동일한 값으로 최소값 도착시 도로 추가,
                        road_check[next_node]= road_check[next_node] + [i]
                        
        node_check=set(node_check) # 지나온길 노드 중복 제거 

        for node in node_check: # 지나온 노드의 도로 확인, 
            for r in road_check[node]:
                road[r]=1
        return arr[D]



        

    def dijkstra(S,D):
        arr=[INF]*(N+1)
        arr[S]=0
        q=[]
        heapq.heappush(q,(0,S))
        while q:
            w,node=heapq.heappop(q)
            if arr[node]<w:
                continue
            for wei,next_node,i in graph[node]:
                if road[i]==1:
                    continue
                cost = w+ wei
                if arr[next_node]>cost:
                    arr[next_node]=cost
                    heapq.heappush(q,(cost,next_node))
        if arr[D]==INF:
            return -1
        else:
            return arr[D]



    first_dijkstra(S,D)

    print(dijkstra(S,D))