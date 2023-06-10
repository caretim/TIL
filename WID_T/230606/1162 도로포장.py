import sys
import heapq
import copy

INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for __ in range(N + 1)]
#이동경로 체크, 각각의 이동시간 확인,

#1. 앞의 이동경로에서 뒤의 최단시간 경로로 이동가능한 도로가 있는지 확인, 
#2. 있다면 그 경로의 시간을 감소,
#3.없다면 최단거리의 경로중 가장 긴 경로의 시간을 0으로 만들기,



for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v, i))
    graph[v].append((w, u, i))


def first_dijkstra(start, end):
    arr = [INF] * (N + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start, list()))
    while q:
        w, city, road_ls = heapq.heappop(q)
        if city == end:
            return w, road_ls
        if arr[city] < w:
            continue
        for wei, next_city, road in graph[city]:
            update_road = copy.deepcopy(road_ls)
            cost = w + wei
            if arr[next_city] > cost:
                arr[next_city] = cost
                update_road.append((road))
                heapq.heappush(q, (cost, next_city, update_road))


def dijkstra(start, end, i):
    arr = [INF] * (N + 1)
    arr[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, city = heapq.heappop(q)
        if arr[city] < w:
            continue
        for wei, next_city, road in graph[city]:
            if road == i:
                continue
            cost = w + wei
            if arr[next_city] > cost:
                arr[next_city] = cost
                heapq.heappush(q, (cost, next_city))
    else:
        return arr[end]


min_dijk, fl = first_dijkstra(1, N)


result = 0
for i in fl:
    new_dijk = dijkstra(1, N, i)
    if new_dijk == INF:
        result = -1
        break

    result = max(result, new_dijk - min_dijk)

print(result)
