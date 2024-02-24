import sys
import heapq
input =sys.stdin.readline

inf = sys.maxsize

n,m = map(int,input().split())


graph = [[] for __ in range(n)]

pc_path =[] 

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u-1].append((w,v-1,i)) # 비용 노드 연결통로 번호
    graph[v-1].append((w,u-1,i)) 
    pc_path.append((i,u,v,0,w)) # 연결통로번호,시작,도착,복구여부

#1번 컴퓨터에서 모든 회선 연결 및 중복되는 구간 제거,
# 회선을 복구하는게아니라 연결복구되는 노드를 출력해야함,

# def dijkstra(start):
#     result = [[] for __ in range(n)]
#     heap = []
#     heapq.heappush(heap,(0,start,""))
#     visited = [inf]*(n)
#     visited[start]= 0
#     while heap:
#         cost,node,path = heapq.heappop(heap)
#         if visited[node]<cost:
#             continue
#         for nextCost,nextNode,nextPath in graph[node]:   
#             w = cost+nextCost
#             if pc_path[nextPath][3]==1: #중복 비용 배제
#                 w-= pc_path[nextPath][4]

#             if visited[nextNode]>w:
#                 visited[nextNode] = nextCost
#                 updatePath= path+str(nextPath)
#                 heapq.heappush(heap,(w,nextNode,updatePath))
#                 result[nextNode]=updatePath
#     return result


# result = set()


# for i in dijkstra(0):
#     for  j in i:
#         result.add(j)

# print(len(result))
# for r in result:
#     print(pc_path[int(r)][1],pc_path[int(r)][2])


def dijkstra(start):
    connect_node = [0]*(n)
    heap = []
    heapq.heappush(heap,(0,start))
    visited = [inf]*(n)
    visited[start]= 0
    while heap:
        cost,node = heapq.heappop(heap)
        if visited[node]<cost:
            continue
        for nextCost,nextNode,nextPath in graph[node]:   
            w = cost+nextCost
            if visited[nextNode]>w:
                visited[nextNode] = w
                connect_node[nextNode]=node
                heapq.heappush(heap,(w,nextNode))
    
    return connect_node


path = dijkstra(0)
print(n-1)
for i in range(1,n):
    print(i+1,path[i]+1)