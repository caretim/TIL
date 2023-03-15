import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

n = int(input())  # 땅의 개수
a, b, c = map(int, input().split())  # 친구 abc의 위치

check = [0] * n

arr = [INF] * (n + 1)

m = int(input())
graph = [[] for __ in range(m)]

for __ in range(m):
    u, v, w = map(int, input().split())  # 시작노드 , 도착노드 , 가중치
    graph[u].append((w, v))
    graph[v].append((w, u))

q = []
heapq.heappush(q, (0, a))
heapq.heappush(q, (0, b))
heapq.heappush(q, (0, c))
arr[a] = 0
arr[b] = 0
arr[c] = 0

while q:
    w, node = heapq.heappop(q)
    if arr[node] < w:
        continue
    for wei, next_node in graph[node]:
        dist = w + wei
        if arr[next_node] > dist:
            arr[next_node] = dist
            heapq.heappush(q, (dist, next_node))

mn = max(arr[1:])  # 시간 최소로 하려면?  딕셔너리로 값지정하고 밸류 기준으로 키 뽑아내기?


for i in range(1, len(arr)):  # 포문으로 동일값 첫번쨰 뽑기?
    if arr[i] == mn:
        print(i)


# a,b,c에서 출발해서  abc노드를 제외한 노드에 도착했을때 최소 값을 각각 넣어주기,
# 3,5,6 동시 출발, -> 제일 먼 곳은 각자의 집에서 출발했을때 최단거리중 가장 큰 곳,
#
