import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for __ in range(n + 1)]

for __ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

x, z = map(int, input().split())

p = int(input())

mn = list((map(int, input().split())))


def dijkstra(start):
    arr = [INF] * (n + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, node = heapq.heappop(q)
        if arr[node] < w:
            continue
        for wei, next_node in graph[node]:
            cost = w + wei
            if arr[next_node] > cost:
                arr[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return arr


arr1 = dijkstra(x)

arr2 = dijkstra(z)

result = INF
for i in mn:
    if result > arr1[i] + arr2[i]:
        result = arr1[i] + arr2[i]


print(result if INF > result else -1)


# 한번에 다익돌리려다가 실패
# def dijkstra(start, end):
#     arr = [INF] * (n + 1)
#     arr[start] = 0
#     q = []
#     last_check = INF  # 중간정점 방문 X 최소 거리
#     heapq.heappush(q, (0, start, 0))
#     while q:
#         w, node, check = heapq.heappop(q)
#         if arr[node] < w:
#             continue
#         for wei, next_node in graph[node]:
#             cost = w + wei
#             if next_node == end:  # 마지막 지점 도착시 check를 통해서 확인
#                 if check == 1:  # 중간 정점 방문함
#                     print(arr)
#                     return cost
#                 elif check == 0:  # 마지막에 도착했지만 중간정점방문 x
#                     if last_check > cost:  #
#                         last_check = cost
#                         heapq.heappush(q, (cost, next_node, check))
#                 continue
#             if arr[next_node] > cost:
#                 arr[next_node] = cost
#                 if check_md[next_node] == 1:
#                     check = 1
#                 heapq.heappush(q, (cost, next_node, check))
#     print(arr)
#     return -1
