import sys
import heapq
import copy

INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for __ in range(N + 1)]
# 도시가 아니라 도로를 막아야함,
# 각 도로에 번호를 넣어준 후, 최초 최소값 구할때 이동하는 도로 리스트에 넣기
# 이후에 방문한 도로만큼, 다익돌려서 경로막았을때 늘어나는 시간 구하기,
# 최초 최소 이동경로만 탐색 -> 검문을 안할때 가는 도로가 최소시간이기 때문,


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
                # if not city == start or next_city == end:
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
