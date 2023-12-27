import sys
import heapq


input = sys.stdin.readline

INF = sys.maxsize


# n, m, c = map(int, input().split())

# # c * x(임의의 정수) = 지하통로 비용 , c의 값이 커질 수록 비용증가,

# # 연결 c*x 이하의 통로 모두 제거 ,

# graph = [[] for __ in range(n + 1)]

# sum_ans = 0
# for __ in range(m):
#     u, v, w = map(int, input().split())
#     u -= 1
#     v -= 1
#     graph[u].append((w, v))
#     graph[v].append((w, u))
#     sum_ans +=w


# def dijkstra(start,graph,x):
#     heap = []
#     heapq.heappush(heap, (0, 0))
#     visited = [INF] * (n)
#     flag=[0] *(n)
#     visited[0] = 0 
#     flag[0]=1
#     while heap:
#         wei, node= heapq.heappop(heap)
#         if visited[node] < wei:
#             continue
#         for w, nextNode in graph[node]:
#             new_wei = w + wei

#         if visited[nextNode] > new_wei:
#             visited[nextNode] = new_wei
#             heapq.heappush(heap, (new_wei, nextNode,flag))
#     print(visited)


# first= dijkstra(0,graph,0)


# for i in first:
#     if i ==0:
#         continue
#     new_graph = 
    

def dijkstra():
    dist = [[INF, set(), i] for i in range(N + 1)] 
    dist[1] = [0, set(), 1]
    pq = []
    pq.append((0, 1)) # (cost, node)
    heapq.heapify(pq)
    while pq:
        _, this_node = heapq.heappop(pq)
        for i in range(len(conj[this_node])):
            next_node, cost = conj[this_node][i]
            via = cost + dist[this_node][0]
            dist[next_node][1].add((this_node, i))
            if via < dist[next_node][0]:
                dist[next_node][0] = via
                heapq.heappush(pq, (via, next_node))
    return dist
    
# N개의 광장, M개의 도로
N, M, C = map(int, input().split())
# 인접 리스트 생성
conj = {i: [] for i in range(1, N + 1)}
d_cost = 0
for i in range(M):
    A, B, D = map(int, input().split())
    d_cost += D
    conj[A].append((B, D))
    conj[B].append((A, D))

# dijkstra로 1을 기준으로한 dijk 리스트 생성
destroy_doro = {i: False for i in range(M)}
temp_dijk = sorted(dijkstra())
min_cost = INF
visit = {i: False for i in range(1, N + 1)}
for i in range(N):
    visit[temp_dijk[i][2]] = True
    for destination, index in temp_dijk[i][1]:
        if visit[destination]:
            d_cost -= conj[destination][index][1]
    # 최종비용 = (C * X이하의 자연수 ) + (남은 도로의 길이)
    total_cost = (C * temp_dijk[i][0]) + d_cost
    min_cost = min(total_cost, min_cost)

print(min_cost)

