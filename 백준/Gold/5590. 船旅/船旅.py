import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start, end):
    arr = [INF] * (n + 1)
    arr[start] = 0
    q = []
    result = -1
    heapq.heappush(q, (0, start))
    while q:
        w, city = heapq.heappop(q)
        if arr[city] < w:
            continue
        if city == end:
            return w
        for wei, next_city in graph[city]:
            cost = w + wei
            if arr[next_city] > cost:
                arr[next_city] = cost
                heapq.heappush(q, (cost, next_city))
    return result


def order(*args):
    if args[0] == False:
        print(dijkstra(args[1], args[2]))
    elif args[0] == True:
        graph[args[1]].append((args[3], args[2]))
        graph[args[2]].append((args[3], args[1]))


n, k = map(int, input().split())

# 첫 번째 숫자가 0이면이 줄은 고객의 주문 표를 나타냅니다.
# 이 행에는 3 개의 정수 0, a, b (1 ≤ a ≤ n, 1 ≤ b ≤ n, a ≠ b)가 공백으로 구분됩니다.
# 이것은 고객이 섬 a를 출발지로하고 섬 b를 목적지로하는 주문 표를 보내 왔음을 나타냅니다.


# 첫 번째 숫자가 1이면이 행은 새로 운항을 시작한 선박의 운항 정보를 나타냅니다.
# 이 행에는 4 개의 정수 1, c, d, e (1 ≤ c ≤ n, 1 ≤ d ≤ n, c ≠ d, 1 ≤ e ≤ 1000000)가 쓰여있다.
# 이것은 섬 c와 섬 d를 왕복하는 선박이 새롭게 운항을 개시하고, 이 선박의 섬 c에서 섬 d로의 운임과 섬 d에서 섬 c로의 운임이 모두 e임을 나타낸다.
# 이 행 이후의 주문표에 대해서는 이 선박도 고려하여 회신을 하여야 한다.

graph = [[] for __ in range(n + 1)]

for __ in range(k):
    a = list(map(int, input().split()))
    order(*a)
