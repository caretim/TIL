import sys
import heapq


input = sys.stdin.readline
INF = sys.maxsize

# 단방향 그래프라 면접장에서 출발하는게 아니라, 도시에서 출발해야함,

n, m, k = map(int, input().split())  # 도시 수 , 도로 수 , 면접장 수

city = [INF] * (n + 1)

graph = [[] for __ in range(n + 1)]


for __ in range(m):
    u, v, w = map(int, input().split())
    # graph[u].append((w, v))
    graph[v].append((w, u))


ct = list(map(int, input().split()))

# check = [INF] * (n + 1)
q = []
for t in ct:
    heapq.heappush(q, (0, t))
    city[t] = 0

while q:
    w, node = heapq.heappop(q)  #
    if city[node] < w:
        continue
    for wei, next_node in graph[node]:
        cost = w + wei
        # if next_node in ct:
        #     if check[start] > cost:
        #         check[start] = cost
        if city[next_node] > cost:
            city[next_node] = cost
            heapq.heappush(
                q, (cost, next_node)
            )  # 힙에 넣는 조건 생각해보기, 한번씩 넣으면 가능한데 , 한번에 다돌릴려면 ?


mn = max(city[1:])


for i in range(1, len(city)):
    if city[i] == mn:
        print(i)
        print(mn)
        break
