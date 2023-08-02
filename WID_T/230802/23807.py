
import sys
import heapq
from  itertools import permutations
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


dist = {}

for node in mn: #중간정점 모두 다익스트라 돌려서 최소 이동값 구함
    dist[node] = dijkstra(node)
dist[x] = dijkstra(x)

# 구한 정점들의 값들을 딕셔너리에 저장 후 각각의 리스트 이동최소 경로를 중복되지 않는 모든 순열의 값으로 지정 
result = INF
for a, b, c in permutations(mn, 3):
    #3개의 순열 조합으로 시작 + 중간지점 3개 + 도착지점 이동거리를 모두 더해서 최소값 찾
    total = dist[x][a] + dist[a][b] + dist[b][c] + dist[c][z]
    if result > total:
        result = total
if result == INF:
    result = -1
print(result)

## 시간초과로 풀리지 않는다 ..ㅋㅋㅋ ..