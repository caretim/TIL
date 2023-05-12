import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline


# 각 교차로 도착시 물의양 추가,
N = int(input())

makeup = list(map(int, input().split()))

M = int(input())

graph = [[] for __ in range(N + 1)]

for __ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


start, end = map(int, input().split())

# 이동거리와 물의 누적량(흠,,직접갖고있게할까?)
def dijkstra(start, end):
    result = -1
    arr = [INF] * (N + 1)
    q = []
    arr[start] = 0
    short = 0

    heapq.heappush(q, (0, -makeup[start - 1], start))
    while q:
        w, water, cross = heapq.heappop(q)
        water = -water
        if arr[cross] < w:
            continue
        for wei, next_cross in graph[cross]:
            distance = w + wei
            added_w = water + makeup[next_cross - 1]
            if next_cross == end:  # 종착에 도착했을때,
                if arr[next_cross] > distance:  # 최단거리로 도착했다면,
                    arr[next_cross] = distance
                    short = added_w
                    result = added_w
                elif arr[next_cross] == distance:  # 최단거리가 같다면
                    if short < added_w:
                        short = added_w
                        result = added_w
            else:
                if arr[next_cross] > distance:
                    arr[next_cross] = distance
                    heapq.heappush(q, (distance, -added_w, next_cross))

    if result == -1:
        return -1
    else:
        return arr[end], short


r = dijkstra(start, end)

if r == -1:
    print(-1)
else:
    print(*r)
